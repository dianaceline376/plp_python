def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Line 3: Adding some numbers 9876\n")
    except Exception as e:
        print(f"Error occurred while creating the file: {e}")
    else:
        print("File created successfully!")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied to read the file!")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 4\n")
            file.write("Line 5: Additional text\n")
            file.write("666\n")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied to append to the file!")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Reading the file again to display appended content
