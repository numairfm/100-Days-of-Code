print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Where do you want to go? Left or right?\n").lower()

if choice1 == "left":
    choice2 = input("You walk towards a river. The next boat stops by in an hour. Do you want to swim or wait?\n").lower()
    if choice2 == "swim":
        print("You get attacked by piranhas. Its game over for you.")
    else:
        choice3 = input("You wait and make it across the river by boat. Three doors stand in front of you. Will you walk through the red, blue, or yellow door?\n").lower()
        if choice3 == "red":
            print("You are burned alive. Its game over for you.")
        elif choice3 == "blue":
            print("You are killed by inhaling toxic gas. Its game over for you.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        else:
            print("Lost in your own indecisiveness, the night falls.\nYou increasingly grow more worried.\nYour mind suffocated in what could be and not what is.\nYou go crazy.\nYou know you have to pick a door but you're scared. You're scared to die.\nYour fear is what leads to your inevitable demise.\nYou collapse under the pressure you put yourself in.\nYou are disappointing. Its game over for you.")
else:
    print("You fall into a hole. Its game over for you.")