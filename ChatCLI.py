from RetrievalChatbot import RetrievalChatbot

def main():
    
    inp = input("Your reply: ")
    bot = RetrievalChatbot("Datasets/marvel.txt")
    while(inp != "bye"):
        print()
        print("Bot: ", bot.get_response(inp))
        print()
        inp=input("Your reply: ")
    
    print()
    print("Bye!\n")

# For CLI use
if  __name__ == "__main__":
    main()

