# Simple rule-based chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

# Main chat loop
print("🤖 Simple Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    reply = chatbot_response(user_input)
    print("Bot:", reply)

    if user_input.lower() in ["bye", "goodbye"]:
        break

print("Chat ended. Have a nice day!")
