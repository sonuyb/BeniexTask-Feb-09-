import time
file_path = "notes.txt"
with open(file_path, "r") as file:
    while True:
        char = file.read(1)
        if char == "":
            break
        print(char, end="")
        time.sleep(0.3)