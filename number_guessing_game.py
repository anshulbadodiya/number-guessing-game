
import random

def get_difficulty():
    """Ask the player to choose a difficulty level."""
    print("\nChoose difficulty:")
    print("  1. Easy   (1–50,  10 attempts)")
    print("  2. Medium (1–100,  7 attempts)")
    print("  3. Hard   (1–200,  5 attempts)")

    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice == "3":
            return 200, 5, "Hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def give_hint(guess, secret):
    """Give a hot/cold style hint based on how close the guess is."""
    diff = abs(guess - secret)
    if diff == 0:
        return ""
    elif diff <= 5:
        return "  (Burning hot! Very close!)"
    elif diff <= 15:
        return "  (Warm! Getting closer.)"
    elif diff <= 30:
        return "  (Cold. Still far away.)"
    else:
        return "  (Freezing! Very far off.)"

def play_game():
    """Main game function — runs one full round."""
    print("\n" + "=" * 40)
    print("     NUMBER GUESSING GAME")
    print("=" * 40)
    print("I'm thinking of a number...")
    print("Can you guess it?\n")

    max_number, max_attempts, level = get_difficulty()
    secret_number = random.randint(1, max_number)
    attempts_used = 0

    print(f"\nOK! I've picked a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        print(f"Attempts remaining: {remaining}")

        # Get a valid number from the player
        while True:
            try:
                guess = int(input(f"Your guess (1–{max_number}): "))
                if 1 <= guess <= max_number:
                    break
                else:
                    print(f"Please enter a number between 1 and {max_number}.")
            except ValueError:
                print("That's not a valid number. Try again.")

        attempts_used += 1

        # Check the guess
        if guess == secret_number:
            print(f"\nCORRECT! The number was {secret_number}.")
            print(f"You guessed it in {attempts_used} attempt(s) on {level} mode!")
            if attempts_used == 1:
                print("Incredible — first try!")
            elif attempts_used <= max_attempts // 2:
                print("Great job! Very efficient.")
            else:
                print("You made it just in time!")
            return True

        elif guess < secret_number:
            hint = give_hint(guess, secret_number)
            print(f"Too LOW!{hint}\n")
        else:
            hint = give_hint(guess, secret_number)
            print(f"Too HIGH!{hint}\n")

    # Player ran out of attempts
    print(f"\nGame over! You've used all {max_attempts} attempts.")
    print(f"The number was {secret_number}. Better luck next time!")
    return False

def main():
    """Entry point — handles replaying the game."""
    print("\nWelcome to the Number Guessing Game!")
    print("Built with Python by Anshul Badodiya\n")

    wins = 0
    losses = 0

    while True:
        result = play_game()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"\nScore — Wins: {wins}  |  Losses: {losses}")

        again = input("\nPlay again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! See you next time.")
            break

if __name__ == "__main__":
    main()
