from flask import Blueprint, render_template
from app.services import get_bitcoin_news, get_bitcoin_price, get_historical_prices, get_quiz_question

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template(
        "index.html",
        bitcoin_price=get_bitcoin_price(),
        bitcoin_news=get_bitcoin_news(),
        historical_prices=get_historical_prices(),
        quiz_question=get_quiz_question(),
    )
