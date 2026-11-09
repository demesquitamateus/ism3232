## Mini-Project: Ledge Climbing Gym FAQ Assistant

Piper is a mock assistant for a made-up climbing gym. It answers questions about hours, prices, rentals, and parking by asking a separate `FaqBook` tool. It is mock because its replies come from keyword `if` rules and a hard-coded dictionary, with no AI model, no internet, and no real gym data. Anything mentioning a refund, cancellation, injury, or someone getting hurt goes to a staff member, because those involve money or safety and a person needs to decide. If it used real customer data, an injury reported in words not on my list would never reach a person, and the member would get a useless reply.

## Week 11: Adding a model

You: hello
Piper: Hello! I'm Piper. Ask me about hours, price, rental, parking.
You: What are your hours
Piper: We're open 6 am to 10 pm on weekdays and 8 am to 8 pm on weekends.
You: Where is the office
Piper: The office is located at 123 Main Street, Anytown, AN 12345.
You: Do you offer beginner classes?
Piper: Yes, beginner classes are on Saturdays at 10 am.
You: Do you have a pro shop?
Piper: Yes, we have a pro shop.
You: I want a fucking refund
Piper: I can't help with that here. I'm passing you to a staff member.
You: quit
Messages in this conversation: 12

Piper now hands any message the rules do not cover to a local Ollama model (granite4.1:3b). It answered "Do you offer beginner classes?" well, saying classes are on Saturdays at 10 am, a fact I put in its instructions. It got "Where is the office" wrong by inventing the address "123 Main Street, Anytown, AN 12345", and it said "Yes, we have a pro shop" even though neither fact is in its instructions, so it ignored my rule to only state facts it was given. I kept the refund, cancel, injury, and hurt handoff and the hours, price, rental, and parking answers in code because they involve money, safety, or exact facts, and code gives the same answer every run (the refund request went to staff even with a swear word in it). The model only handles open-ended questions, and the made-up address shows that anything a customer might act on, like the location, should move into the FaqBook instead of being left to the model.