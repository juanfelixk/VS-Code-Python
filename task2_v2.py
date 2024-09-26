import random
import os

stat = {
    "health": 100,
    "score": 0,
}

def load_game(file_name):
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                stat["health"] = int(lines[0].strip())
                stat["score"] = int(lines[1].strip())
            return stat
        except IndexError:
            return None

def save_game(file_name):
    with open(file_name, "w") as file:
        file.write(f"{stat["health"]}\n")
        file.write(f"{stat["score"]}\n")
    print("Gameplay successfully saved.")

def gameplay():
    while True:
        print("""
Choose an action:
    1. Explore the area (chance of gaining or losing health).
    2. Get some rest (gain health).
    3. Save and exit.
""")
        choice = int(input("Enter your choice of action: " ))
        if choice == 1:
            i = random.randint(0,1)
            if i == 0:
                stat["score"] += 10
                print(f"You found a treasure! + 10 points. Your current score is {stat['score']}.")
            else:
                stat["health"] -= 10
                print(f"You encountered a monster! - 10 health. Your current health is {stat['health']}.")
        elif choice == 2:
            if stat["health"] <= 95:
                stat["health"] += 5
            print(f"You gained 5 health. Your current health is {stat['health']}.")
        elif choice == 3:
            save_game("data.txt")
            print("Your gameplay has been successfully saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        
        if stat["health"] <= 0:
            print("Your current health is 0. Game over!")
            break

def main():
    print("Welcome!")
    user_input = input(("Load previous game? (y/n): ")).lower()
    if user_input == "y":
        x = load_game("data.txt")
        if x is None:
            print("No game data found. Starting a new game.")
            stat = {
            "health": 100,
            "score": 0
        }
        gameplay()
    elif user_input == "n":
        stat = {
            "health": 100,
            "score": 0
        }
        print("Starting new gameplay.")
        gameplay()
    else:
        print("Invalid choice!")

main()