def validate_order(symbol, side, order_type, quantity, price, stop_price=None):
    if not symbol:
        raise ValueError("Symbol is required")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    # allow MARKET, LIMIT, and STOP_LIMIT (mapped to STOP order type)
    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

    if order_type == "STOP_LIMIT":
        if stop_price is None or price is None:
            raise ValueError("Both stop_price and price are required for STOP_LIMIT orders")

    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0")

    if stop_price is not None and stop_price <= 0:
        raise ValueError("Stop price must be greater than 0")