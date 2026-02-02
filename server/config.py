"""
Lucid - Central Configuration
============================
All configuration variables in one place. Edit these to customize behavior.
"""

# =============================================================================
# NEWS SOURCES CONFIG
# =============================================================================
# Easy to add/remove sources. Each source needs:
#   - name: Display name
#   - url: RSS feed URL
#   - lean: Political lean ("left", "center", "right", "international")
#
# Note: Some RSS feeds may require different parsing. Test after adding new sources.

NEWS_SOURCES = [
    # === Wire Services / Center ===
    {"name": "AP News", "url": "http://associated-press.s3-website-us-east-1.amazonaws.com/topnews.xml", "lean": "center"},
    {"name": "Reuters", "url": "https://feeds.reuters.com/Reuters/worldNews", "lean": "center"},
    {"name": "Reuters Business", "url": "https://feeds.reuters.com/reuters/businessNews", "lean": "center"},
    {"name": "PBS NewsHour", "url": "https://www.pbs.org/newshour/feeds/rss/headlines", "lean": "center"},
    {"name": "The Hill", "url": "https://thehill.com/feed/", "lean": "center"},
    {"name": "Axios", "url": "https://api.axios.com/feed/", "lean": "center"},
    {"name": "USA Today", "url": "https://rssfeeds.usatoday.com/usatoday-NewsTopStories", "lean": "center"},
    {"name": "USA Today Sports", "url": "https://rssfeeds.usatoday.com/usatodaycomsports-topstories", "lean": "center"},
    {"name": "ABC News", "url": "https://abcnews.go.com/abcnews/topstories", "lean": "center"},
    {"name": "CBS News", "url": "https://www.cbsnews.com/latest/rss/main", "lean": "center"},
    {"name": "NBC News", "url": "https://feeds.nbcnews.com/nbcnews/public/news", "lean": "center"},

    # === Left-leaning ===
    {"name": "NPR", "url": "https://feeds.npr.org/1001/rss.xml", "lean": "left"},
    {"name": "NPR Science", "url": "https://feeds.npr.org/1007/rss.xml", "lean": "left"},
    {"name": "NPR Technology", "url": "https://feeds.npr.org/1019/rss.xml", "lean": "left"},
    {"name": "The Guardian", "url": "https://www.theguardian.com/us-news/rss", "lean": "left"},
    {"name": "Guardian Tech", "url": "https://www.theguardian.com/technology/rss", "lean": "left"},
    {"name": "Guardian Sports", "url": "https://www.theguardian.com/sport/rss", "lean": "left"},
    {"name": "MSNBC", "url": "https://www.msnbc.com/feeds/latest", "lean": "left"},
    {"name": "Washington Post", "url": "https://feeds.washingtonpost.com/rss/politics", "lean": "left"},
    {"name": "WaPo Business", "url": "https://feeds.washingtonpost.com/rss/business", "lean": "left"},
    {"name": "NY Times", "url": "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml", "lean": "left"},
    {"name": "NY Times Tech", "url": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml", "lean": "left"},
    {"name": "NY Times Science", "url": "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml", "lean": "left"},
    {"name": "NY Times Sports", "url": "https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml", "lean": "left"},
    {"name": "Vox", "url": "https://www.vox.com/rss/index.xml", "lean": "left"},
    {"name": "HuffPost", "url": "https://www.huffpost.com/section/politics/feed", "lean": "left"},
    {"name": "Slate", "url": "https://slate.com/feeds/all.rss", "lean": "left"},
    {"name": "The Atlantic", "url": "https://www.theatlantic.com/feed/all/", "lean": "left"},
    {"name": "Salon", "url": "https://www.salon.com/feed/", "lean": "left"},

    # === Right-leaning ===
    {"name": "Fox News", "url": "https://moxie.foxnews.com/google-publisher/politics.xml", "lean": "right"},
    {"name": "Fox Business", "url": "https://moxie.foxnews.com/google-publisher/business.xml", "lean": "right"},
    {"name": "Fox Sports", "url": "https://moxie.foxnews.com/google-publisher/sports.xml", "lean": "right"},
    {"name": "Fox Tech", "url": "https://moxie.foxnews.com/google-publisher/tech.xml", "lean": "right"},
    {"name": "NY Post", "url": "https://nypost.com/news/feed/", "lean": "right"},
    {"name": "NY Post Sports", "url": "https://nypost.com/sports/feed/", "lean": "right"},
    {"name": "Washington Times", "url": "https://www.washingtontimes.com/rss/headlines/news/politics/", "lean": "right"},
    {"name": "Daily Wire", "url": "https://www.dailywire.com/feeds/rss.xml", "lean": "right"},
    {"name": "Breitbart", "url": "https://feeds.feedburner.com/breitbart", "lean": "right"},
    {"name": "The Federalist", "url": "https://thefederalist.com/feed/", "lean": "right"},
    {"name": "National Review", "url": "https://www.nationalreview.com/feed/", "lean": "right"},
    {"name": "Washington Examiner", "url": "https://www.washingtonexaminer.com/feed", "lean": "right"},
    {"name": "Daily Caller", "url": "https://dailycaller.com/feed/", "lean": "right"},
    {"name": "Newsmax", "url": "https://www.newsmax.com/rss/Newsfront/1/", "lean": "right"},

    # === International ===
    {"name": "BBC", "url": "https://feeds.bbci.co.uk/news/world/rss.xml", "lean": "international"},
    {"name": "BBC Tech", "url": "https://feeds.bbci.co.uk/news/technology/rss.xml", "lean": "international"},
    {"name": "BBC Science", "url": "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml", "lean": "international"},
    {"name": "BBC Sports", "url": "https://feeds.bbci.co.uk/sport/rss.xml", "lean": "international"},
    {"name": "Al Jazeera", "url": "https://www.aljazeera.com/xml/rss/all.xml", "lean": "international"},
    {"name": "DW News", "url": "https://rss.dw.com/rdf/rss-en-all", "lean": "international"},
    {"name": "France24", "url": "https://www.france24.com/en/rss", "lean": "international"},
    {"name": "The Economist", "url": "https://www.economist.com/united-states/rss.xml", "lean": "international"},
    {"name": "Sky News", "url": "https://feeds.skynews.com/feeds/rss/world.xml", "lean": "international"},
    {"name": "ABC Australia", "url": "https://www.abc.net.au/news/feed/51120/rss.xml", "lean": "international"},
    {"name": "Japan Times", "url": "https://www.japantimes.co.jp/feed/", "lean": "international"},

    # === Tech Focused ===
    {"name": "TechCrunch", "url": "https://techcrunch.com/feed/", "lean": "center"},
    {"name": "Ars Technica", "url": "https://feeds.arstechnica.com/arstechnica/index", "lean": "center"},
    {"name": "The Verge", "url": "https://www.theverge.com/rss/index.xml", "lean": "center"},
    {"name": "Wired", "url": "https://www.wired.com/feed/rss", "lean": "center"},
    {"name": "Engadget", "url": "https://www.engadget.com/rss.xml", "lean": "center"},
    {"name": "CNET", "url": "https://www.cnet.com/rss/news/", "lean": "center"},

    # === Business / Economy ===
    {"name": "CNBC", "url": "https://www.cnbc.com/id/100003114/device/rss/rss.html", "lean": "center"},
    {"name": "Bloomberg", "url": "https://feeds.bloomberg.com/markets/news.rss", "lean": "center"},
    {"name": "MarketWatch", "url": "https://feeds.marketwatch.com/marketwatch/topstories/", "lean": "center"},
    {"name": "Financial Times", "url": "https://www.ft.com/rss/home", "lean": "international"},
    {"name": "Business Insider", "url": "https://www.businessinsider.com/rss", "lean": "center"},

    # === Sports ===
    {"name": "ESPN", "url": "https://www.espn.com/espn/rss/news", "lean": "center"},
    {"name": "ESPN NFL", "url": "https://www.espn.com/espn/rss/nfl/news", "lean": "center"},
    {"name": "ESPN NBA", "url": "https://www.espn.com/espn/rss/nba/news", "lean": "center"},
    {"name": "CBS Sports", "url": "https://www.cbssports.com/rss/headlines/", "lean": "center"},
    {"name": "Bleacher Report", "url": "https://bleacherreport.com/articles/feed", "lean": "center"},
    {"name": "Sports Illustrated", "url": "https://www.si.com/rss/si_topstories.rss", "lean": "center"},

    # === Science / Health ===
    {"name": "Science Daily", "url": "https://www.sciencedaily.com/rss/all.xml", "lean": "center"},
    {"name": "Live Science", "url": "https://www.livescience.com/feeds/all", "lean": "center"},
    {"name": "Space.com", "url": "https://www.space.com/feeds/all", "lean": "center"},
    {"name": "Scientific American", "url": "http://rss.sciam.com/ScientificAmerican-Global", "lean": "center"},
    {"name": "Stat News", "url": "https://www.statnews.com/feed/", "lean": "center"},

    # === Entertainment / Culture ===
    {"name": "Variety", "url": "https://variety.com/feed/", "lean": "center"},
    {"name": "Rolling Stone", "url": "https://www.rollingstone.com/feed/", "lean": "left"},
    {"name": "Entertainment Weekly", "url": "https://ew.com/feed/", "lean": "center"},
    {"name": "Deadline", "url": "https://deadline.com/feed/", "lean": "center"},
    {"name": "Hollywood Reporter", "url": "https://www.hollywoodreporter.com/feed/", "lean": "center"},
]

# =============================================================================
# CLUSTERING CONFIG
# =============================================================================
# Controls how articles are grouped into stories
# Embeddings are generated via Jina AI API (free tier: 1M tokens/month)
# Get your free API key at: https://jina.ai/embeddings/

# Cosine similarity threshold for clustering (0.0 - 1.0)
# Higher = stricter matching, fewer clusters
# Lower = looser matching, more articles grouped together
SIMILARITY_THRESHOLD = 0.45  # Lower threshold to catch differently-worded coverage

# Minimum number of different sources required for a story to be included
# Higher = only stories covered by multiple outlets (more significant)
MIN_SOURCES_FOR_STORY = 2

# Maximum articles to consider for clustering (performance)
MAX_ARTICLES_FOR_CLUSTERING = 2000  # Process more articles per run

# How many hours back to look for articles to cluster
CLUSTERING_WINDOW_HOURS = 96  # 4 days instead of 2

# =============================================================================
# RELEVANCE SCORING CONFIG
# =============================================================================
# Controls how stories are ranked (higher score = more prominent)

# Weight for number of sources (more sources = more important)
RELEVANCE_WEIGHT_SOURCES = 15  # Points per source

# Weight for political diversity (covered across spectrum = bigger story)
RELEVANCE_WEIGHT_DIVERSITY = 20  # Points per unique lean (left/center/right/international)

# Weight for recency (hours old reduces score)
RELEVANCE_WEIGHT_RECENCY = 2  # Points lost per hour old

# Base score for all stories
RELEVANCE_BASE_SCORE = 50

# =============================================================================
# SYNTHESIS CONFIG
# =============================================================================
# Controls LLM-based summary generation

# LLM model to use
# For Ollama: "llama3.1:8b", "llama3.1:70b", "mistral:7b", "mixtral:8x7b"
# For Groq: "llama-3.1-8b-instant", "llama-3.3-70b-versatile", "mixtral-8x7b-32768"
# For Together: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
LLM_MODEL = "llama-3.3-70b-versatile"

# LLM provider: "ollama" (local), "groq", "together"
LLM_PROVIDER = "groq"

# API keys (only needed for cloud providers)
# Get your free Groq key at: https://console.groq.com/keys
# In production, set GROQ_API_KEY environment variable instead
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")  # Set via environment variable
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY", "")  # Get from https://api.together.xyz/

# Ollama settings
OLLAMA_HOST = "http://localhost:11434"

# Generation parameters
MAX_TOKENS = 3000  # Max length of generated summaries (doubled for deeper analysis)
TEMPERATURE = 0.3  # Lower = more deterministic (0.0 - 1.0)

# Retry settings for API calls
LLM_MAX_RETRIES = 3
LLM_RETRY_DELAY = 2  # seconds

# =============================================================================
# APP CONFIG
# =============================================================================
# Web application settings

# How often to automatically refresh data (in hours)
REFRESH_INTERVAL_HOURS = 6

# Maximum stories to keep in the database
MAX_STORIES_IN_FEED = 100  # More stories in the feed

# Stories per page for pagination
STORIES_PER_PAGE = 12  # More per page

# Flask settings
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
FLASK_DEBUG = True

# =============================================================================
# DATABASE CONFIG
# =============================================================================
# SQLite database settings
# In production (Render), uses /data mount for persistence

# Check for Render disk mount first, then fall back to local
if os.path.exists("/data"):
    DATABASE_PATH = "/data/news_bench.db"
else:
    DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "news_bench.db")

# =============================================================================
# SCRAPING CONFIG
# =============================================================================
# RSS feed scraping settings

# Request timeout in seconds
REQUEST_TIMEOUT = 15

# User agent for requests
USER_AGENT = "Lucid/1.0 (News Aggregator; +https://github.com/lucid)"

# Delay between requests to same domain (seconds)
REQUEST_DELAY = 1.0

# Maximum age of articles to scrape (hours)
MAX_ARTICLE_AGE_HOURS = 120  # 5 days for more comprehensive coverage

# =============================================================================
# CATEGORY CONFIG
# =============================================================================
# Valid story categories for classification

VALID_CATEGORIES = [
    "politics",   # US politics, elections, policy
    "economy",    # Markets, business, finance
    "tech",       # Technology, AI, startups
    "sports",     # All sports coverage
    "culture",    # Entertainment, pop culture, arts
    "world",      # International news, foreign affairs
    "science",    # Science, health, climate, environment
    "other",      # Fallback for uncategorized stories
]
