import random

def number_guessing_game():
    number = random.randint(1, 10)
    attempts = 0
    print("Guess a number between 1 and 10.")
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess == number:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
            elif guess < number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
