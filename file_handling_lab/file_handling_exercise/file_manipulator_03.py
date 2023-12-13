import os

while True:
    line = input().split("-")
    if line[0] == "End":
        break

    command, file = line[0], line[1],

    if command == "Create":
        with open(file, "w") as file:
            pass

    elif command == "Add":
        content = line[2]

        with open(file, "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old_str = line[2]
        new_str = line[3]
        try:
            with open(file, "r+") as file:
                text = file.read()
                text = text.replace(old_str, new_str)

                file.seek(0)
                file.write(text)

        except FileNotFoundError:
            print(f"An error occurred")

    elif command == "Delete":
        try:
            os.remove(file)

        except FileNotFoundError:
            print(f"An error occurred")
