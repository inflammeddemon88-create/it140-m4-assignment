"""A higher/lower number guessing game that prompts for valid bounds and provides guess feedback.

Input:
    Lower bound (integer), upper bound (integer), and user numerical guesses (integers).

Process:
    Validates lower bound < upper bound via loop, generates a target random number 
    using randint, validates guesses are within bounds, and uses decision branching 
    within a game loop to give high/low feedback until guessed correctly.

Output:
    Welcome and prompt messages, error feedback for invalid bounds/guesses, 
    too-low/too-high hints, and victory output.
"""

# === Imports ===
from random import randint


# === Main Function ===
def main() -> None:
    """Run the optional higher/lower game practice program."""

    print("Welcome to the higher/lower game, Bella!")

    # Obtain and validate the lower and upper bounds.
    while True:
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))

        if lower_bound < upper_bound:
            break
        print("The lower bound must be less than the upper bound.")

    # Generate a random number from the valid range using randint.
    target_number = randint(lower_bound, upper_bound)

    # Obtain and validate the player's first guess.
    prompt = f"Great, now guess a number between {lower_bound} and {upper_bound}: "

    # Repeat until the player guesses the random number.
    while True:
        user_guess = int(input(prompt))

        # Validate guess is within bounds
        if user_guess < lower_bound or user_guess > upper_bound:
            print(f"Your guess must be between {lower_bound} and {upper_bound}.")
            prompt = "Guess another number: "
            continue

        # Give too-low or too-high feedback for incorrect valid guesses.
        if user_guess < target_number:
            print("Nope, too low.")
            prompt = "Guess another number: "
        elif user_guess > target_number:
            print("Nope, too high.")
            prompt = "Guess another number: "
        else:
            # Display a success message after the correct guess.
            print("You got it!")
            break


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# Southern New Hampshire University. (2026). IT-140: Introduction to Scripting.
