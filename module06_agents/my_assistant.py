# my_assistant.py
# Author: Mateus De Mesquita

# Words that mean a person must handle the request (money or safety).
HANDOFF_WORDS = ["refund", "cancel", "injury", "hurt"]


class FaqAssistant:
    """A mock FAQ assistant. Its replies come from simple rules, not from AI."""

    def __init__(self, name, instructions, faq):
        """Set up one assistant with its own name, instructions, tool, and history."""
        self.name = name  # what the assistant is called
        self.instructions = instructions  # stored now; a real model uses it in Week 11
        self.faq = faq  # the tool we were handed (composition)
        self.history = []  # each assistant starts with its own empty list

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
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
        # A question the tool couldn't match: say so, don't invent an answer.
        if "?" in text:
            return (
                "I don't have an answer to that yet. "
                f"I can answer questions about {self.faq.list_topics()}."
            )
        return f"I'm not sure how to help with that. Ask me about {self.faq.list_topics()}."

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False
