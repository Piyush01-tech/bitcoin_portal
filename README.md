<div align="center">

# ₿ Bitcoin Portal

**A real-time Bitcoin dashboard built with Flask — live price, news, historical charts, and a knowledge quiz.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-f7931a?style=for-the-badge)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Piyush01-tech/bitcoin_portal?style=for-the-badge&color=f7931a)](https://github.com/Piyush01-tech/bitcoin_portal)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💰 **Live Price** | Real-time BTC/USD price via CoinGecko |
| 📈 **Price Chart** | Interactive 30-day history with Chart.js |
| 📰 **News Feed** | Latest Bitcoin headlines from CoinTelegraph |
| 🧠 **Quiz** | Test your Bitcoin knowledge |
| 🌙 **Dark Theme** | Warm dark UI with amber accents |
| 📱 **Responsive** | Works on desktop, tablet, and mobile |

---

## 🚀 Quick Start

### Prerequisites

- [Python 3.10+](https://python.org/downloads/)

### Installation

```bash
# Clone the repository
git clone https://github.com/Piyush01-tech/bitcoin_portal.git
cd bitcoin_portal

# Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
```

Open **http://127.0.0.1:5000** in your browser. 🎉

> **Note:** No API keys required — news and price data use free, open endpoints.

---

## 📁 Project Structure

```
bitcoin_portal/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   └── services.py
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
└── run.py
```

---

## 🔧 Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| `FLASK_DEBUG` | No | Set to `true` for development mode |
| `SECRET_KEY` | No | Flask secret key (auto-generated in dev) |

---

## 🛠 Built With

- **[Flask](https://flask.palletsprojects.com/)** — Lightweight Python web framework
- **[Chart.js](https://www.chartjs.org/)** — Beautiful, responsive charts
- **[CoinGecko](https://www.coingecko.com/)** — Real-time & historical Bitcoin pricing
- **[CoinTelegraph](https://cointelegraph.com/)** — Latest crypto news (via RSS)

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ☕ by [Piyush01-tech](https://github.com/Piyush01-tech)**

</div>
