with open("my_file.txt") as f:
    contents = f.read()
    print(contents)

with open("my_file.txt", mode="w") as f:
    contents = f.write("New text.")
    print(contents)

with open("my_file.txt", mode="a") as f:
    contents = f.write("New text.")
    print(contents)