import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
    COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
    NEWS_RSS_URL = "https://api.rss2json.com/v1/api.json"
    NEWS_RSS_FEED = "https://cointelegraph.com/rss/tag/bitcoin"
    DEBUG = os.environ.get("FLASK_DEBUG", "false").lower() in ("true", "1", "yes")
