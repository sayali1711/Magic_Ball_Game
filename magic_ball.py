import random
answers=["It is certain.","As I see it, yes.","Reply hazy, try again.","Don't count on it.","It is decidedly so.","Most likely.","Ask again later."," My reply is no.","Without a doubt.","Outlook good.","Better not tell you now"," My sources say no.","Yes – definitely."," Yes.","Cannot predict now.","Outlook not so good.","You may rely on it.","Signs point to yes.","Concentrate and ask again.","Very doubtful"]
print("HELLO! I am a MAGIC BALL, what is your name?")
name=input()
print("Hello",name)
def magicball():
    print("lets begin!!")
    print("Hey",name,"Ask me a question")
    qs=input()
    print(answers[random.randint(0,len(answers)-1)])
    print("I hoped you are satisfied with the answer")
    replay()      
def replay():
    print("Would you like to play again? (y/n)")
    a=input()
    if(a=="y" or a=="Y" or a=="yes" or a=="Yes" or a=="YES"):
        magicball()
    elif(a=="n" or a=="N" or a=="no" or a=="No" or a=="NO"):
        exit()
    else:
        print("I didn't get it !! enter again")
        replay()
magicball()        
    
          

