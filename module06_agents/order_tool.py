# order_tool.py
# Mateus De Mesquita

class OrderLookup:
    """A tool that knows about orders and their statuses. It knows nothing about chatting."""


    def __init__(self, orders):
        """Store the orders this tool can look up."""
        self.orders = orders

    def find_order_id(self, text):
        """Return the first known order ID mentioned in text, or None."""
        for order_id in self.orders:
            if order_id in text.upper():
                return order_id
        return None
    
    def find_status(self, text):
        """Return the status of one order, or None if there is no such order."""
        if order_id in self.orders:
            return self.orders[order_id]
        return None
