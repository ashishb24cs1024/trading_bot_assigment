import argparse
from rich import print
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from trading_bot.client import BinanceClient
from trading_bot.orders import OrderService
from trading_bot.validators import validate_order
from trading_bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True, help="MARKET, LIMIT, or STOP_LIMIT")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="required for LIMIT and STOP_LIMIT")
    parser.add_argument("--stop-price", type=float, help="required for STOP_LIMIT")

    args = parser.parse_args()

    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price, getattr(args, 'stop_price', None))

        print("\n[cyan]Order Request Summary[/cyan]")
        print(vars(args))

        client = BinanceClient().get_client()
        service = OrderService(client)

        order = service.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=getattr(args, 'stop_price', None)
        )

        print("\n[green]ORDER SUCCESS[/green]")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Quantity: {order.get('executedQty')}")
        print(f"Average Price: {order.get('avgPrice')}")

    except Exception as e:
        print(f"\n[red]ORDER FAILED[/red] {str(e)}")
        logger.error(str(e))


if __name__ == "__main__":
    main()