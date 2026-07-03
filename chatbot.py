def chatbot():
    print("===================================")
    print("     WELCOME TO BASIC CHATBOT")
    print("===================================")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user == "i am fine":
            print("Bot: That's great to hear!")

        elif user == "what is your name":
            print("Bot: My name is ChatBot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()