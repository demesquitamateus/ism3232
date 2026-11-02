from my_assistant import FaqAssistant
from my_tool import FaqBook


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    faq = FaqBook({"hours": "6 am to 10 pm.", "price": "A day pass is $18."})
    return FaqAssistant("Piper", "Be clear.", faq)


def test_tool_finds_known_topic():
    faq = FaqBook({"hours": "6 am to 10 pm."})
    assert faq.find_topic("What are your HOURS?") == "hours"


def test_tool_returns_none_for_unknown_topic():
    faq = FaqBook({"hours": "6 am to 10 pm."})
    assert faq.find_topic("Do you sell shoes?") is None


def test_price_question_uses_the_tool():
    assistant = make_assistant()
    assert assistant.respond("What is the price of a day pass?") == "A day pass is $18."


def test_unanswered_question_gets_a_helpful_reply():
    assistant = make_assistant()
    reply = assistant.respond("Do you sell shoes?")
    assert "don't have an answer" in reply
    assert "hours" in reply


def test_refund_goes_to_a_person():
    assistant = make_assistant()
    assert "staff member" in assistant.respond("I want a refund for my pass")


def test_unknown_statement_gets_a_safe_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("Nice weather today")


def test_history_records_role_and_content():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What are your hours?")
    assert len(assistant.history) == 4
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"


def test_two_assistants_keep_separate_histories():
    first = make_assistant()
    second = make_assistant()
    first.respond("hello")
    assert len(first.history) == 2
    assert len(second.history) == 0
