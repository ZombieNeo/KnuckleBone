from cgi import print_form
from random import *
from tabnanny import check





#VARIABLES
player_name = input("enter your name ")
player_score = 0
Com_name = "BOZO"
Com_score = 0
coinflip = randint(1,2)#WHO GOES FIRST?????????????????????????????
player_roll = int
Com_roll = int
Player_row_1 = 0
Player_row_2 = 0
Player_row_3 = 0
Com_row_1 = 0
Com_row_2 = 0
Com_row_3 = 0
#VARIABLES





#INTRO
print("Welcome! "+player_name)
print("To decide who goes first we will flip a coin...")
print(coinflip)
if coinflip == 2:
    print(player_name+" goes first!")
    player_roll = randint(1,6)
    Player_roll_1 = player_roll #STORES ROLL AS VAR
    print(player_name+ " rolled a "+str(player_roll))
    pass
else:
    print(Com_name+" goes first!")
    Com_roll = randint(1,6)
    Com_roll_1 = Com_roll #STORES ROLL AS VAR
    print(Com_name+ " rolled a "+str(Com_roll))
    pass

#INTRO

#GAME

def Placement():
  Location=input(" Where do you want to place this die? ")
  if Location == 1:
    if Player_row_1 >= 3:
        print("THIS ROW IS FULL! ")
        pass
    Player_row_1 =+ 1 #STATES THERE IS 1 DIE IN ROW
    if Location == 2:
        if Player_row_2 >= 3:
            print("THIS ROW IS FULL! ")
            pass
    Player_row_2 =+ 1 #STATES THERE IS 1 DIE IN ROW
    if Location == 3:
        if Player_row_3 >= 3:
            print("THIS ROW IS FULL! ")
            pass
    Player_row_3 =+ 1 #STATES THERE IS 1 DIE IN ROW

Placement()
    




#GAME