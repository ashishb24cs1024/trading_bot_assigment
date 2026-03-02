## Binance Futures Testnet Trading Bot
📖 Description

A modular, command-line based trading bot built in Python that integrates with the Binance Futures Testnet (USDT-M).

The application supports Market, Limit, and Stop-Limit orders with proper input validation, structured logging, and robust exception handling. The architecture follows separation of concerns to ensure readability, maintainability, and reliability.

## ✨ Features

Support for BUY and SELL order sides

Order types supported:

MARKET

LIMIT

STOP_LIMIT (Stop-Limit)

CLI interface using argparse

Input validation before order execution

Structured logging of API requests and responses

Exception handling for API and network failures

Modular code organization

## 🏗 Project Structure
binance-futures-trading-bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
⚙️ Installation
1️⃣ Clone the repository
git clone <your-repository-url>
cd binance-futures-trading-bot
2️⃣ Create virtual environment (optional but recommended)

macOS / Linux

python -m venv venv
source venv/bin/activate

Windows

python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
🔐 Environment Configuration

Create a .env file in the root directory:

API_KEY=your_api_key
API_SECRET=your_api_secret

Ensure your Binance Futures Testnet account is active and funded with testnet balance.

## ▶️ Usage
Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
Stop-Limit Order
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 59000 --stop-price 59500
## 📝 Logging

All API interactions, including request details, responses, and error messages, are logged to:

trading_bot.log

This ensures traceability and easier debugging.

## 🛡 Assumptions

Binance Futures Testnet account is active

Valid API credentials are provided

Sufficient testnet balance is available

