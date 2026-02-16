import random

# Generate a random number between 1 and 100 for the computer
num_pc = random.randint(1, 100)

# Initialize the user's number and the attempt counter
num = 0
cont = 0

# Main loop: continues until the user guesses the correct number
while num != num_pc:

    # Input validation loop: ensures the user enters a valid positive number
    while True:
        try:
            num = int(input("Enter a number: "))
            if num > 0:
                break  # Valid number, exit validation loop
            else:
                print("ERROR: Invalid number")
        except ValueError:
            print("ERROR: You must enter a number, not a letter")

    # Give hints based on the user's guess
    if num < num_pc:
        print("Higher")
    elif num > num_pc:
        print("Lower")
    else:
        print("You guessed it!")

    # Increase the attempt counter
    cont += 1

# Display the total number of attempts
print("Number of attempts:", cont)