import logging

logger = logging.getLogger(__name__)


class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price} {stop_price}")

            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            elif order_type == "STOP_LIMIT":
                # Binance futures uses type "STOP" for stop-limit orders
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="STOP",
                    quantity=quantity,
                    price=price,
                    stopPrice=stop_price,
                    timeInForce="GTC"
                )
            else:
                raise ValueError("Unsupported order type")

            logger.info(f"Order response: {order}")
            return order

        except Exception as e:
            logger.error(f"Order failed: {str(e)}")
            raise