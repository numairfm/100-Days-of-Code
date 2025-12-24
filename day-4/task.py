import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
pick = int(input("Whats your play? 0 for rock, 1 for paper, 2 for scissors: "))
cpu_pick = random.randint(0, 2)

if pick > 2 or pick < 0:
    print("Sorry, that's not a valid choice.")
else:
    print(f"Your pick:\n{game_images[pick]}")
    print(f"CPU pick:\n{game_images[cpu_pick]}")

if pick == 0 and cpu_pick == 1:
    print("You lose!")
elif pick == 0 and cpu_pick == 2:
    print("You win!")
elif pick == 1 and cpu_pick == 0:
    print("You win!")
elif pick == 1 and cpu_pick == 2:
    print("You lose!")
elif pick == 2 and cpu_pick == 1:
    print("You win!")
elif pick == 2 and cpu_pick == 0:
    print("You lose!")
elif pick == cpu_pick:
    print("Its a tie!")
