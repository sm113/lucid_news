#!/usr/bin/env python3
"""
Lucid - Unified Entry Point
===========================
Single entry point for all Lucid operations: server, pipeline, and deployment.

Usage:
    python main.py              # Start web server (default)
    python main.py --serve      # Start web server
    python main.py --pipeline   # Run full pipeline (scrape + cluster + synthesize)
    python main.py --scrape     # Only scrape news sources
    python main.py --cluster    # Only cluster recent articles
    python main.py --synthesize # Only synthesize new clusters
    python main.py --stats      # Show database statistics
    python main.py --cleanup 7  # Remove data older than 7 days
    python main.py --deploy     # Production deployment (gunicorn)
"""

import argparse
import sys
import os
import time
from datetime import datetime


def print_banner():
    """Print startup banner."""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   LUCID                                                   ║
║   Neutral News Aggregator & Analyzer                      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)


def run_scrape():
    """Run the scraping step."""
    from pipeline import scraper
    print("\n[STEP 1] Scraping news sources...")
    print("-" * 50)
    scraper.scrape_all_sources()


def run_cluster():
    """Run the clustering step."""
    from pipeline import clusterer
    print("\n[STEP 2] Clustering related articles...")
    print("-" * 50)
    return clusterer.run_clustering()


def run_synthesize(clusters=None):
    """Run the synthesis step."""
    from pipeline import synthesizer
    print("\n[STEP 3] Synthesizing stories with AI...")
    print("-" * 50)
    synthesizer.run_synthesis(clusters)


def run_pipeline():
    """Run the full pipeline: scrape -> cluster -> synthesize."""
    from server import database

    start_time = time.time()
    print_banner()

    print(f"Starting pipeline at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Initialize database
    database.init_database()

    # Step 1: Scrape
    run_scrape()

    # Step 2: Cluster
    clusters = run_cluster()

    # Step 3: Synthesize (if we have clusters)
    if clusters:
        run_synthesize(clusters)
    else:
        print("\n[WARNING] No new clusters to synthesize")

    # Summary
    elapsed = time.time() - start_time
    stats = database.get_stats()

    print("\n" + "=" * 60)
    print("[PIPELINE COMPLETE]")
    print("=" * 60)
    print(f"  Total articles: {stats['total_articles']}")
    print(f"  Total stories:  {stats['total_stories']}")
    print(f"  Sources:        {stats['unique_sources']}")
    print(f"  Time elapsed:   {elapsed:.1f} seconds")
    print("=" * 60)
    print("\nDone! Run 'python main.py' to start the web interface.\n")


def run_server():
    """Start the Flask web server."""
    from server import database
    from server.app import main as app_main

    database.init_database()
    app_main()


def run_deploy():
    """Production deployment with gunicorn."""
    from server import database

    port = os.environ.get('PORT', '10000')

    # Initialize database (fast)
    print("[START] Initializing database...")
    database.init_database()

    stats = database.get_stats()
    print(f"[START] Database ready: {stats['total_articles']} articles, {stats['total_stories']} stories")

    # Start gunicorn immediately (don't block on pipeline)
    # The scheduler in app.py will run the pipeline periodically
    # Or use /api/refresh to trigger manually
    print(f"[START] Starting gunicorn on port {port}...")
    print("[START] Pipeline will run via scheduler or /api/refresh")

    os.execvp('gunicorn', [
        'gunicorn', 'server.app:app',
        '--bind', f'0.0.0.0:{port}',
        '--workers', '1',
        '--threads', '2',
        '--timeout', '300'
    ])


def show_stats():
    """Show current database statistics."""
    from server import database

    database.init_database()
    stats = database.get_stats()

    print("\n[Lucid Statistics]")
    print("-" * 40)
    print(f"  Total articles:     {stats['total_articles']}")
    print(f"  Total stories:      {stats['total_stories']}")
    print(f"  Unique sources:     {stats['unique_sources']}")
    print(f"  Last article:       {stats['last_article_at'] or 'Never'}")
    print(f"  Last story:         {stats['last_story_at'] or 'Never'}")
    print()


def cleanup(days: int = 7):
    """Clean up old data."""
    from server import database

    database.init_database()
    print(f"\n[CLEANUP] Removing data older than {days} days...")
    database.cleanup_old_data(days=days)
    print("Done!")


# =============================================================================
# CLI INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Lucid - Neutral News Aggregator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                 Start the web server (default)
  python main.py --serve         Start the web server
  python main.py --pipeline      Run full pipeline (scrape + cluster + synthesize)
  python main.py --scrape        Only scrape news sources
  python main.py --cluster       Only cluster recent articles
  python main.py --synthesize    Only synthesize new clusters
  python main.py --stats         Show database statistics
  python main.py --cleanup 7     Remove data older than 7 days
  python main.py --deploy        Production deployment (gunicorn)
        """
    )

    parser.add_argument('--serve', action='store_true', help='Start web server (default)')
    parser.add_argument('--pipeline', action='store_true', help='Run full pipeline')
    parser.add_argument('--scrape', action='store_true', help='Only run scraping step')
    parser.add_argument('--cluster', action='store_true', help='Only run clustering step')
    parser.add_argument('--synthesize', action='store_true', help='Only run synthesis step')
    parser.add_argument('--stats', action='store_true', help='Show database statistics')
    parser.add_argument('--cleanup', type=int, metavar='DAYS', help='Remove data older than N days')
    parser.add_argument('--deploy', action='store_true', help='Production deployment (gunicorn)')

    args = parser.parse_args()

    # Import database for commands that need it
    from server import database

    # Handle specific commands
    if args.stats:
        show_stats()
    elif args.cleanup:
        cleanup(args.cleanup)
    elif args.scrape:
        print_banner()
        database.init_database()
        run_scrape()
    elif args.cluster:
        print_banner()
        database.init_database()
        run_cluster()
    elif args.synthesize:
        print_banner()
        database.init_database()
        run_synthesize()
    elif args.pipeline:
        run_pipeline()
    elif args.deploy:
        run_deploy()
    else:
        # Default: start web server
        run_server()


if __name__ == "__main__":
    main()
