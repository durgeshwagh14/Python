''' 
We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user. 
'''

import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
youstr = input("Enter your choice:")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake", -1:"Water",0:"Gun"}

you =youDict[youstr]

print(f"You Chose {reverseDict[you]}\n Computer Chose {reverseDict[computer]}")

if(computer == you):
  print("Its a draw")

else :

  if(computer==-1 and you == 1):
    print("You Win🏆")

  elif(computer==-1 and you == 0):
    print("you Lose 😒")

  elif(computer==1 and you == -1):
    print("you Lose 😒")

  elif(computer==1 and you == 0):
    print("You Win🏆")

  elif(computer==0 and you == -1):
    print("You Win🏆")

  elif(computer==0 and you == -1):
    print("You Lose ")

  else:
    print("something went wrong")


print("End the Game")

