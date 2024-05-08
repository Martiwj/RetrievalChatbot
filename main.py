from RetrievalChatbot import RetrievalChatbot
from tester import Chatbot

if  __name__ == "__main__":
    
    inp = input("Your reply: ")
    bot = RetrievalChatbot("scripts/marvel.txt")
    bot1 = Chatbot("scripts/marvel.txt")
    while(inp != "bye"):
        print()
        print("Bot: ", bot.get_response(inp))
        print()
        inp=input("Your reply: ")
    
    print()
    print("Bye!\n")