#!/usr/bin/env python3
"""
Startup script for Render deployment.
Starts gunicorn immediately. Pipeline runs via scheduler or /api/refresh.
"""
import os

def main():
    port = os.environ.get('PORT', '10000')

    # Initialize database (fast)
    print("[START] Initializing database...")
    import database
    database.init_database()

    stats = database.get_stats()
    print(f"[START] Database ready: {stats['total_articles']} articles, {stats['total_stories']} stories")

    # Start gunicorn immediately (don't block on pipeline)
    # The scheduler in app.py will run the pipeline periodically
    # Or use /api/refresh to trigger manually
    print(f"[START] Starting gunicorn on port {port}...")
    print("[START] Pipeline will run via scheduler or /api/refresh")

    os.execvp('gunicorn', [
        'gunicorn', 'app:app',
        '--bind', f'0.0.0.0:{port}',
        '--workers', '1',
        '--threads', '2',
        '--timeout', '300'
    ])

if __name__ == '__main__':
    main()
