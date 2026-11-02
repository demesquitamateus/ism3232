# my_tool.py
# Author: Mateus De Mesquita


class FaqBook:
    """A tool that knows answers to common gym questions. It knows nothing about chatting."""

    def __init__(self, answers):
        """Store the answers this tool can look up."""
        # answers is a dict like {"hours": "We're open ..."}; keeping it on self
        # lets every other method in this object read it later.
        self.answers = answers

    def find_topic(self, text):
        """Return the first known topic mentioned in text, or None."""
        # Loop over the topic names (the dict's keys).
        for topic in self.answers:
            # Lowercase the text so "HOURS" and "hours" both match.
            if topic in text.lower():
                return topic
        # Nothing matched, so return None instead of guessing.
        return None

    def answer_for(self, topic):
        """Return the answer for one topic, or None if the topic is unknown."""
        if topic in self.answers:
            return self.answers[topic]
        return None

    def list_topics(self):
        """Return the topic names as one readable string."""
        # join glues the keys together: "hours, price, rental, parking"
        return ", ".join(self.answers)
