#!/usr/bin/env python3
"""
Lucid - Category Migration Script
=================================
Backfills existing stories with category classifications using LLM.

Usage:
    python -m pipeline.migrate_categories           # Migrate all uncategorized stories
    python -m pipeline.migrate_categories --limit 50  # Migrate up to 50 stories
    python -m pipeline.migrate_categories --dry-run   # Preview without saving
"""

import argparse
import time
import json
import re
from typing import Optional

from server import database
from server.config import (
    LLM_MODEL,
    LLM_PROVIDER,
    GROQ_API_KEY,
    TOGETHER_API_KEY,
    OLLAMA_HOST,
    TEMPERATURE,
    LLM_MAX_RETRIES,
    LLM_RETRY_DELAY,
    VALID_CATEGORIES
)
from pipeline.prompts import CATEGORY_PROMPT


def call_ollama(prompt: str) -> Optional[str]:
    import requests
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={
                "model": LLM_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": TEMPERATURE,
                    "num_predict": 50
                }
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json().get('response', '').strip()
    except Exception as e:
        print(f"Ollama error: {e}")
        return None


def call_groq(prompt: str) -> Optional[str]:
    import requests
    if not GROQ_API_KEY:
        return None
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
            json={
                "model": LLM_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": TEMPERATURE,
                "max_tokens": 50
            },
            timeout=30
        )
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Groq error: {e}")
        return None


def call_together(prompt: str) -> Optional[str]:
    import requests
    if not TOGETHER_API_KEY:
        return None
    try:
        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={"Authorization": f"Bearer {TOGETHER_API_KEY}"},
            json={
                "model": LLM_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": TEMPERATURE,
                "max_tokens": 50
            },
            timeout=30
        )
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Together error: {e}")
        return None


def call_llm(prompt: str) -> Optional[str]:
    providers = {"ollama": call_ollama, "groq": call_groq, "together": call_together}
    func = providers.get(LLM_PROVIDER)
    if not func:
        return None

    for attempt in range(LLM_MAX_RETRIES):
        result = func(prompt)
        if result:
            return result
        time.sleep(LLM_RETRY_DELAY)
    return None


def classify_story(headline: str, consensus: str) -> str:
    """Classify a story into a category using LLM."""
    prompt = CATEGORY_PROMPT.format(
        headline=headline,
        consensus=consensus[:1000] if consensus else "No summary available."
    )

    response = call_llm(prompt)
    if not response:
        return "other"

    # Clean and validate response
    category = response.lower().strip()
    # Remove any punctuation or extra text
    category = re.sub(r'[^a-z]', '', category)

    if category in VALID_CATEGORIES:
        return category
    return "other"


def run_migration(limit: int = 100, dry_run: bool = False):
    """Migrate uncategorized stories."""
    print("\n" + "=" * 60)
    print("LUCID - Category Migration")
    print("=" * 60)

    database.init_database()

    # Get stories without proper categories
    stories = database.get_stories_without_category(limit=limit)

    if not stories:
        print("\nNo stories need categorization!")
        return

    print(f"\nFound {len(stories)} stories to categorize")
    if dry_run:
        print("[DRY RUN MODE - No changes will be saved]")

    success_count = 0
    category_counts = {}

    for i, story in enumerate(stories):
        print(f"\n[{i+1}/{len(stories)}] Processing story {story['id']}...")
        print(f"  Headline: {story['synthesized_headline'][:60]}...")

        category = classify_story(
            story['synthesized_headline'],
            story.get('consensus', '')
        )

        print(f"  Category: {category}")

        # Track stats
        category_counts[category] = category_counts.get(category, 0) + 1

        if not dry_run:
            if database.update_story_category(story['id'], category):
                success_count += 1
            else:
                print(f"  ERROR: Failed to update story {story['id']}")

        # Rate limiting - respect API limits
        time.sleep(0.5)

    # Summary
    print("\n" + "=" * 60)
    print("MIGRATION COMPLETE")
    print("=" * 60)
    print(f"  Total processed: {len(stories)}")
    if not dry_run:
        print(f"  Successfully updated: {success_count}")
    print("\n  Category distribution:")
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        print(f"    {cat}: {count}")


def main():
    parser = argparse.ArgumentParser(description="Backfill story categories")
    parser.add_argument('--limit', type=int, default=100,
                        help="Maximum stories to process (default: 100)")
    parser.add_argument('--dry-run', action='store_true',
                        help="Preview without saving changes")
    args = parser.parse_args()

    run_migration(limit=args.limit, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
