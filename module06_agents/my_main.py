# my_main.py
# Author: Mateus De Mesquita

from my_assistant import FaqAssistant
from my_tool import FaqBook
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Piper, a front-desk assistant for Ledge Climbing Gym.
Answer in one short sentence.
Beginner classes are on Saturdays at 10 am.
Children under 14 must have an adult in the gym.
Only state facts that appear in these instructions.
If you do not know, say exactly: I do not know; please ask a staff member.
Never promise refunds, bookings, or schedule changes."""

ANSWERS = {
    "hours": "We're open 6 am to 10 pm on weekdays and 8 am to 8 pm on weekends.",
    "price": "A day pass is $18 and a monthly membership is $79.",
    "rental": "Shoe rental is $6 and a harness is $5.",
    "parking": "Free parking is behind the building. Overflow is on Marsh Street.",
}

faq = FaqBook(ANSWERS)
model = OllamaModel(MODEL_NAME)
assistant = FaqAssistant("Piper", INSTRUCTIONS, faq, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
