# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

guests = []

with open("/Users/mmrha/PycharmProjects/Mail_Merge/Input/Names/invited_names.txt") as f:
    invited_guests = f.readlines()

for names in invited_guests:
    name = names.strip("\n")
    guests.append(name)

replace_text = "[name]"

with open("/Users/mmrha/PycharmProjects/Mail_Merge/Input/Letters/starting_letter.txt") as start:
    letter = start.read()

for names in guests:
    updated_letter = letter.replace(replace_text, names)
    with open(f"/Users/mmrha/PycharmProjects/Mail_Merge/Output/ReadyToSend/{names}.txt", mode="w") as new_file:
        new_file.write(updated_letter)
