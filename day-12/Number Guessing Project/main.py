import art
import random

DIFFICULTIES = ["easy", "hard"]

def game():
    number = random.randint(1, 100)
    print(art.logo)

    def setup_mode():
        while True:
            lives = 0
            chosen_difficulty = input("Choose your difficulty!\n- Easy\n- Hard\n> ").lower()
            if chosen_difficulty not in DIFFICULTIES:
                print("Not a valid difficulty!")
            else:
                if chosen_difficulty == "easy":
                    lives = 10
                    print(f"Chosen difficulty is {chosen_difficulty}. You start with {lives} lives!")
                    return lives
                elif chosen_difficulty == "hard":
                    lives = 5
                    print(f"Chosen difficulty is {chosen_difficulty}. You start with {lives} lives!")
                    return lives


    def validate_int_input():
        while True:
            try:
                chosen_number = int(input("Enter a number between 1 and 100:\n> "))
                return chosen_number
            except ValueError:
                print("That's not an integer!")

    game_lives = setup_mode()

    while game_lives > 0:

        guessed_number = validate_int_input()

        if guessed_number == number:
            print("You guessed the number!")
            return "Win"
        else:
            if guessed_number > (number + 40):
                print("Way too high!")
            elif guessed_number < (number - 40):
                print("Way too low!")
            elif guessed_number > (number + 20):
                print("Too high!")
            elif guessed_number < (number - 20):
                print("Too low!")
            elif guessed_number > (number + 10):
                print("A bit too high!")
            elif guessed_number < (number - 10):
                print("A bit too low!")
            elif guessed_number > (number + 5):
                print("A tiny bit too high!")
            elif guessed_number < (number - 5):
                print("A tiny bit too low!")
            elif guessed_number > number:
                print("Close, but still high!")
            elif guessed_number < number:
                print("Close, but still low!")


        game_lives -= 1
        print(f"You have {game_lives} lives left!")

    print("You lose!")
    return "Lose"



while True:
    game()

    restart_question = input("Play again? (y or n)\n> ").lower()
    if restart_question == "y":
        print("\n" * 20)
        continue
    else:
        print("Thanks for playing!")
        break