import art
import game_data
import random

def initial_choose_accounts():
    account_1 = random.choice(game_data.data)
    account_2 = random.choice(game_data.data)

    while account_1["name"] == account_2["name"]:
        account_2 = random.choice(game_data.data)

    return account_1, account_2

def choose_account(account):
    account_1 = account
    account_2 = random.choice(game_data.data)

    while account_1["name"] == account_2["name"]:
        account_2 = random.choice(game_data.data)

    return account_1, account_2

def guess_person(account_1, account_2):
    global score
    a = account_1
    b = account_2

    while True:
        guess = input(f"Who has more followers? A or B? Score: {score}\n> ").lower()

        if guess not in ["a", "b"]:
            print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
            print(art.vs)
            print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")

            print("Please enter either 'a' or 'b'.\n")

        elif guess == "a":
            guess = a
            other = b

            return guess, other
        elif guess == "b":
            guess = b
            other = a

            return guess, other

def who_is_bigger(guess, other):
    guessed_person = guess
    other_person = other

    if guessed_person['follower_count'] > other_person['follower_count']:
        pass
    elif guessed_person['follower_count'] < other_person['follower_count']:
        return 0
    return 1

def setup():
    first_account, second_account = initial_choose_accounts()

    print(f"Compare A: {first_account['name']}, {first_account['description']}, from {first_account['country']}")
    print(art.vs)
    print(f"Compare B: {second_account['name']}, {second_account['description']}, from {second_account['country']}")

    guessed_person, other = guess_person(first_account, second_account)
    result = who_is_bigger(guessed_person, other)

    return guessed_person, other, result

score = 0

def game():
    global score
    print(art.logo)
    guessed_person, other, result = setup()

    if result == 0:
        return score
    else:
        score += 1


    while True:
        first_account, second_account = choose_account(guessed_person)

        print(f"Compare A: {first_account['name']}, {first_account['description']}, from {first_account['country']}")
        print(art.vs)
        print(f"Compare B: {second_account['name']}, {second_account['description']}, from {second_account['country']}")

        guessed_person, other = guess_person(first_account, second_account)

        result = who_is_bigger(guessed_person, other)

        if result == 0:
            return score
        else:
            score += 1

        print(f"Score: {score}")

final_result = game()
print(f"Final score: {final_result}")

while True:
    retry = input("Do you want to play again? [Y/N]\n").lower()
    if retry == "n":
        break
    else:
        score = 0
        final_result = game()
        print(f"Final score: {final_result}")

