# test_my_assistant.py
# Author: Mateus De Mesquita
# These tests use fake models only, so they pass with Ollama switched off.

from mock_model import MockModel
from my_assistant import SAFE_REPLY, FaqAssistant
from my_tool import FaqBook

ANSWERS = {
    "hours": "We're open 6 am to 10 pm on weekdays and 8 am to 8 pm on weekends.",
    "price": "A day pass is $18 and a monthly membership is $79.",
}


class NoneModel:
    """A model that never has an answer, like Ollama when it is switched off."""

    def reply(self, instructions, history):
        return None


class RecordingModel:
    """A model that remembers what it was asked, so tests can see if it was called."""

    def __init__(self):
        self.calls = []

    def reply(self, instructions, history):
        self.calls.append((instructions, list(history)))
        return "model answer"


def make_assistant(model):
    return FaqAssistant("Piper", "Be brief.", FaqBook(ANSWERS), model)


def test_assistant_stores_the_model():
    model = MockModel()
    assert make_assistant(model).model is model


def test_other_messages_go_to_the_model():
    reply = make_assistant(MockModel()).respond("Do you offer lessons?")
    assert reply == "I'm not sure how to help with that. I can check an order or stock."


def test_model_gets_instructions_and_history():
    model = RecordingModel()
    make_assistant(model).respond("Do you offer lessons?")
    instructions, history = model.calls[0]
    assert instructions == "Be brief."
    assert history[-1] == {"role": "user", "content": "Do you offer lessons?"}


def test_model_with_no_answer_gets_safe_reply():
    assert make_assistant(NoneModel()).respond("Do you offer lessons?") == SAFE_REPLY


def test_tool_answers_before_the_model():
    model = RecordingModel()
    reply = make_assistant(model).respond("What are your hours?")
    assert reply == ANSWERS["hours"]
    assert model.calls == []


def test_handoff_happens_in_code_not_in_the_model():
    model = RecordingModel()
    reply = make_assistant(model).respond("I want a refund")
    assert "staff member" in reply
    assert model.calls == []


def test_safe_reply_is_saved_in_history():
    bot = make_assistant(NoneModel())
    bot.respond("Do you offer lessons?")
    assert bot.history[-1] == {"role": "assistant", "content": SAFE_REPLY}
