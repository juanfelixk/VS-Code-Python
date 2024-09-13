import random
num = random.randint(2,99)
attempt = 0

print(num)

print("\nWELCOME TO GUESS THE NUMBER!")

print("""
INSTRUCTIONS:
    1. This game will generate a secret integer between 1-100 exclusive.
    2. Guess the secret integer.
    3. You have 3 attempts before losing this game. 
""")

while attempt < 3:
    if attempt == 0:
        print("Input your first guess!")
        answer = int(input())
        attempt += 1
        if answer == num:
            print("Your first guess {} is correct! Congratulations!".format(answer))
        else:
            if answer < num:
                print("\nYour first guess is too small!")
            elif answer > num:
                print("\nYour first guess is too big!")
            print("Your first guess is incorrect! Please try again.")
    else:    
        print("\nInput your next guess!")
        answer = int(input())
        attempt += 1
        if answer == num:
            print("\nYou got it correct at attempt {}! Congratulations!\n".format(attempt))
        else:
            if attempt < 3:
                if answer < num:
                    print("\nYour guess is too small!")
                elif answer > num:
                    print("\nYour guess is too big!")
                print("Your guess is still incorrect! Please try again.")
            elif attempt == 3:
                print("\nYou have used your 3 attempts. The secret integer is {}. Game over!\n".format(num))