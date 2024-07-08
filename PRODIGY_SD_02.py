import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    user_guess = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while user_guess != number_to_guess:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the right number: {number_to_guess}")
                print(f"It took you {attempts} {'attempt' if attempts == 1 else 'attempts'} to guess the number.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()