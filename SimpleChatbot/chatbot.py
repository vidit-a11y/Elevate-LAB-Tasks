def chatbot():
 
    print("Hi! I'm a simple chatbot. Type 'bye' to exit.")
    print("You can ask me things like 'how are you?' or 'what is your name?'.")
    print("-" * 20) 

    while True:
      
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there!")

        elif "how are you" in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing great! Thanks for asking.")

        elif "what is your name" in user_input:
            print("Bot: I don't have a name yet. You can name me!")

        elif "what is" in user_input and "+" in user_input:
             print("Bot: I'm not a calculator, but I'll try my best in the future!")

        elif "bye" in user_input or "quit" in user_input:
            print("Bot: Goodbye! Have a great day.")
            break 
        else:
            print("Bot: I'm not sure how to answer that. I'm still learning!")

if __name__ == "__main__":
    chatbot()