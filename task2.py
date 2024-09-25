def save_data(file_name):
    data_input = input("Enter the data to be saved: ")
    with open(file_name, "a") as file:
        file.write(data_input + "\n")
    print(f"Data successfully saved to {file_name}")

def open_data():
    file_input = input("Enter the name of the file (.txt) to be opened: ")
    try:
        with open(file_input, "r") as file:
            content = file.read()  
        if content:
            print("Here is the content of the requested file:")
            print(content)
        else:
            print("The file is curently empty")
    except FileNotFoundError:
        print(f"The file {file_input} does not exist. Please try again")

def main():
    while True:
        print("""
Choose an action from the options below:
    1. Save new data.
    2. Open existing data.
    3. Exit
""")
        choice = int(input("Input your choice: "))
        if choice == 1:
            save_data("data.txt")
        elif choice == 2:
            open_data()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

        
main()