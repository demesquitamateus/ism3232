# my_assistant.py
# Author: Mateus De Mesquita

# Words that mean a person must handle the request (money or safety).
HANDOFF_WORDS = ["refund", "cancel", "injury", "hurt"]

SAFE_REPLY = (
    "I don't have an answer to that. Please ask a staff member at the front desk."
)


class FaqAssistant:
    """An FAQ assistant. Rules run first; a model handles everything else."""

    def __init__(self, name, instructions, faq, model):
        """Set up one assistant with its own name, instructions, tool, model, and history."""
        self.name = name  # what the assistant is called
        self.instructions = instructions  # now sent to the model on every call
        self.faq = faq  # the tool we were handed (composition)
        self.model = model  # the model we were handed (composition)
        self.history = []  # each assistant starts with its own empty list

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Use a rule when one applies. Otherwise ask the model."""
        text = user_message.lower()
        # Safety and money come first, so a person sees these requests.
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a staff member."
        # Ask the tool whether the message is about a topic it knows.
        topic = self.faq.find_topic(user_message)
        if topic is not None:
            return self.faq.answer_for(topic)
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me about {self.faq.list_topics()}."
        # No rule applied, so the model gets the message.
        return self.model_reply()

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the model has none."""
        reply = self.model.reply(self.instructions, self.history)
        if reply is None or reply.strip() == "":
            return SAFE_REPLY
        return reply

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False
