HANDOFF_WORDS = ["address", "payment", "card"]


class SupportChatbot:
    def __init__(self, name, instructions, order_tool):
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "bot", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()
        if self.needs_human(text):
            return "I cannot help with that here. I am passing you off to my human pet."

        if "order" in text:
            return self.order_reply(user_message)
        if "hello" in text:
            return f"Hello~ I am {self.name}. I can check an order status for you."
        return "I am not sure how to respond to that. I can check for an order status."

    def needs_human(self, text):
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def order_reply(self, user_message):
        order_id = self.order.tool.find_order_id(user_message)
        if order_id is None:
            return "I could not find an order ID in your message. Please provide a valid order ID."
        status = self.order_tool.find_status(order_id)
        return f"Order {order_id} is {status}."
