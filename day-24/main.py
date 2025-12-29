import json

print(
    "Hello, this is a program to test data persistence. Im lazy to integrate it into snake."
)


def main():
    file_path = "./store/data.json"
    set_mode = input("Create, append or read data?: 'c', 'a', 'r'\n> ").lower()

    if set_mode == "c":
        data = {}

        while True:
            key = input("key: ")
            value = input("value: ")
            data[key] = value
            if input("new key? (y, n): ").lower() == "n":
                break

        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Dump generated successfully, check {file_path}")

    elif set_mode == "a":
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        while True:
            key = input("key: ")
            value = input("value: ")
            data[key] = value
            if input("new key? (y, n): ").lower() == "n":
                break

        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Dump generated successfully, check data.json")

    else:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        keys = []
        for key in data.keys():
            keys.append(key)
        print(f"Available keys {keys}")


main()
