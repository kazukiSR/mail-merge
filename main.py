PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as letterFile:
    letter = letterFile.read()
    for rawName in names:
        name = rawName.strip()
        readyLetter = letter.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as file:
            file.write(readyLetter)
