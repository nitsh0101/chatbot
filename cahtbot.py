import nltk
from nltk.chat.util import Chat, reflections

# Download the NLTK data if not already downloaded
nltk.download("punkt")

# Define the chat pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"what is your name",
        ["I'm just a chatbot. You can call me Chotu.",]
    ],
    [
        r"how are you",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm sorry, I don't provide weather information.",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand. Can you please rephrase?",]
    ],
]

def chatbot():
    print("Hi! I'm your chatbot. Type 'exit' to end the conversation.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chat.respond(user_input)
        print("Bot:", response)

if _name_ == "_main_":
    chatbot()
