# my_main.py
# Author: Mateus De Mesquita

from my_assistant import FaqAssistant
from my_tool import FaqBook

ANSWERS = {
    "hours": "We're open 6 am to 10 pm on weekdays and 8 am to 8 pm on weekends.",
    "price": "A day pass is $18 and a monthly membership is $79.",
    "rental": "Shoe rental is $6 and a harness is $5.",
    "parking": "Free parking is behind the building. Overflow is on Marsh Street.",
}

faq = FaqBook(ANSWERS)
assistant = FaqAssistant(
    "Piper",
    "You answer common questions for Ledge Climbing Gym.",
    faq,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
