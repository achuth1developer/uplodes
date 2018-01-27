#simple snake and ladder game
import random
count=0
while (count<=100):
    a=input("enter 'r' to roll dice")
    if(a=='r'):
            r=random.randint(1,6)
            count=count+r
            print(r)
    if(count==8):
            count=37
            print("u climed the ladder",count)
    elif(count==11):
            count=2
            print("snake bites u",count)
            
    
    if(count==13):
            count=34
            print("u climed the ladder",count)
    elif(count==25):
            count=4
            print("snake bites u",count)
            
    if(count==38):
            count=9
            print("snake bites u",count)
    elif(count==40):
            count=68
            print("u climed the ladder",count)

    if(count==52):
            count=81
            print("u climed the ladder",count)
    elif(count==65):
            count=46
            print("snake bites u",count)

    if(count==76):
            count=97
            print("u climed the ladder",count)
    elif(count==89):
            count=70
            print("snake bites u",count)
            
    if(count==93):
            count=64
            print("snake bites u",count)
    elif(count==100):
            count=100
            print("hey you wom the game",count)


            



