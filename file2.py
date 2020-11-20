from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

my_first_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(my_first_bot)
trainer.train("chatterbot.corpus.english")

flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(my_first_bot.get_response(user_response)!=None):
                print(my_first_bot.get_response(user_response))
            else:
                print("ROBO: ",end="")
                print(my_first_bot.get_response(user_response))
    else:
        flag=False
        print("ROBO: Bye! take care..")   