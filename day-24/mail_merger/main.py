def main():
    path_letter = "./Input/Letters/starting_letter.txt"
    path_names = "./Input/Names/invited_names.txt"
    output_path = "./Output/ReadyToSend/"

    with open(path_letter, "r") as f:
        contents = f.read()
        print(contents)

    with open(path_names, "r") as f:
        names = f.read()
        names = [line for line in names.splitlines()]

    for i, name in enumerate(names):
        final_output_path = f"{output_path}{name}.txt"
        mail = contents.replace("[name]", name)
        with open(final_output_path, "w") as f:
            f.write(mail)


main()
