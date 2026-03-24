import logging
import random
from datetime import datetime, timezone

import requests
from flask import current_app

logger = logging.getLogger(__name__)
REQUEST_TIMEOUT = 10


def get_bitcoin_price():
    url = f"{current_app.config['COINGECKO_API_URL']}/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    try:
        response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        price = response.json()["bitcoin"]["usd"]
        return f"{price:,.2f}"
    except (requests.RequestException, KeyError) as exc:
        logger.error("Failed to fetch Bitcoin price: %s", exc)
        return "N/A"


def get_bitcoin_news():
    rss_url = current_app.config["NEWS_RSS_URL"]
    feed_url = current_app.config["NEWS_RSS_FEED"]
    try:
        response = requests.get(
            rss_url, params={"rss_url": feed_url}, timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
        data = response.json()
        if data.get("status") != "ok":
            return []
        articles = []
        for item in data.get("items", [])[:6]:
            articles.append({
                "title": item.get("title", ""),
                "description": item.get("description", ""),
                "url": item.get("link", "#"),
                "source": item.get("author", "CoinTelegraph"),
                "date": item.get("pubDate", "")[:10],
                "thumbnail": item.get("thumbnail", ""),
            })
        return articles
    except requests.RequestException as exc:
        logger.error("Failed to fetch Bitcoin news: %s", exc)
        return []


def get_historical_prices():
    url = f"{current_app.config['COINGECKO_API_URL']}/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": 30, "interval": "daily"}
    try:
        response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        result = {}
        for timestamp_ms, price in data.get("prices", []):
            date_str = datetime.fromtimestamp(
                timestamp_ms / 1000, tz=timezone.utc
            ).strftime("%Y-%m-%d")
            result[date_str] = round(price, 2)
        return result
    except (requests.RequestException, KeyError) as exc:
        logger.error("Failed to fetch historical prices: %s", exc)
        return {}


QUIZ_QUESTIONS = [
    {
        "question": "What is the maximum supply of Bitcoin?",
        "answers": ["21 million", "100 million", "1 billion"],
        "correct": 0,
    },
    {
        "question": "Who is credited with creating Bitcoin?",
        "answers": ["Satoshi Nakamoto", "Vitalik Buterin", "Nick Szabo"],
        "correct": 0,
    },
    {
        "question": "What consensus mechanism does Bitcoin use?",
        "answers": ["Proof of Work", "Proof of Stake", "Delegated Proof of Stake"],
        "correct": 0,
    },
    {
        "question": "In what year was Bitcoin launched?",
        "answers": ["2009", "2011", "2013"],
        "correct": 0,
    },
    {
        "question": "What is a Bitcoin halving?",
        "answers": [
            "Block reward is cut in half",
            "Transaction fees double",
            "Network speed halves",
        ],
        "correct": 0,
    },
    {
        "question": "What is the smallest unit of Bitcoin called?",
        "answers": ["Satoshi", "Wei", "Gwei"],
        "correct": 0,
    },
]


def get_quiz_question():
    return random.choice(QUIZ_QUESTIONS)
