#!/usr/bin/env python3
"""
Startup script for Render deployment.
Runs ONLY the scraper (fast), then starts gunicorn.
Clustering/synthesis happens via /api/refresh or scheduler.
"""
import os
import sys

def main():
    port = os.environ.get('PORT', '10000')

    # Initialize database
    print("[START] Initializing database...")
    import database
    database.init_database()

    # Check if we have data
    stats = database.get_stats()
    print(f"[START] Current: {stats['total_articles']} articles, {stats['total_stories']} stories")

    # If no articles, run ONLY the scraper (it's fast, no ML)
    if stats['total_articles'] == 0:
        print("[START] No articles - running scraper only...")
        try:
            import scraper
            scraper.scrape_all_sources()
            stats = database.get_stats()
            print(f"[START] Scraper done: {stats['total_articles']} articles")
        except Exception as e:
            print(f"[START] Scraper error (continuing anyway): {e}")

    # Start gunicorn
    print(f"[START] Starting gunicorn on port {port}...")
    os.execvp('gunicorn', [
        'gunicorn', 'app:app',
        '--bind', f'0.0.0.0:{port}',
        '--workers', '1',
        '--threads', '2',
        '--timeout', '120'
    ])

if __name__ == '__main__':
    main()
