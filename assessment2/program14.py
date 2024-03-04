class Notes:
    FILENAME = "notes.txt"  
 
    @staticmethod
    def write(note):
        """Write the note to the file (overwriting existing content)."""
        with open(Notes.FILENAME, "w") as file:
            file.write(note)
        print("Note written successfully!")
 
    @staticmethod
    def read():
        """Read the entire file contents and return them."""
        try:
            with open(Notes.FILENAME, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "No notes found."
 
    @staticmethod
    def append(note):
        """Append the note to the end of the file."""
        with open(Notes.FILENAME, "a") as file:
            file.write("\n" + note)
        print("Note appended successfully!")
 
def main():
    while True:
        print("\nMenu:")
        print("1. Write Note (Overwrite existing)")
        print("2. Add more Notes (Append)")
        print("3. Read Notes")
        print("4. Exit")
 
        choice = input("Enter your choice (1/2/3/4): ")
 
        if choice == "1":
            note = input("Enter your note: ")
            Notes.write(note)
        elif choice == "2":
            note = input("Enter the additional note: ")
            Notes.append(note)
        elif choice == "3":
            print(Notes.read())
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
 
if __name__ == "__main__":
    main()
 