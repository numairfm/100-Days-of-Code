
while True:
    try:
        age = int(input("How old are you? "))
    except ValueError as e:
        print("Please enter a valid age. Error", e)
    else:
        if age >= 18:
            print(f"You can drive at age {age}.")
        else:
            print(f"You cant drive at age {age}.")
