from RetrievalChatbot import RetrievalChatbot

if  __name__ == "__main__":
    
    inp = input("Your reply: ")
    bot = RetrievalChatbot("scripts/marvel.txt")
    while(inp != "bye"):
        print()
        print("Bot: ", bot.get_response(inp))
        print()
        inp=input("Your reply: ")
    
    print()
    print("Bye!\n")
