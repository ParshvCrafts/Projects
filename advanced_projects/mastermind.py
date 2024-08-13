
import random

def display_instructions():
    print("\033c")
    print("\n** Mastermind Instructions **")
    print("1. The computer will generate a secret code consisting of 4 colors.")
    print("2. Your task is to guess the correct color code within 10 attempts.")
    print("3. The available colors are: (R)ed, (G)reen, (B)lue, (Y)ellow, (W)hite, (P)urple.")
    print("4. Enter the first letter of each color (e.g., 'RGBY') to make a guess.")
    print("5. After each guess, you'll receive feedback:")
    print("   - 'Correct color, correct place' indicates both color and position match.")
    print("   - 'Correct color, wrong place' indicates the color is correct, but the position is wrong.")
    print("6. If you guess the code correctly within 10 attempts, you win!")
    print("-" * 60 + "\n")

def generate_code(colors):
    return [random.choice(colors) for _ in range(4)]

def get_feedback(guess, code):
    correct_color_place = sum([1 for i in range(4) if guess[i] == code[i]])
    correct_color = sum([min(guess.count(color), code.count(color)) for color in set(guess)]) - correct_color_place
    return correct_color_place, correct_color

def play_game():
    print("Welcome to the Mastermind Game!")
    if input("Do you need instructions? [Y/N]: ").strip().lower() == "y":
        display_instructions()

    colors = ["R", "G", "B", "Y", "W", "P"]
    color_code = generate_code(colors)
    attempts = 1

    while attempts <= 10:
        guess = input(f"Attempt {attempts}/10: Enter your guess (e.g., 'RGBY'): ").strip().upper()
        if len(guess) != 4 or any(c not in colors for c in guess):
            print("Invalid input. Please enter 4 valid colors using their initials (e.g., 'RGBY').")
            continue

        attempts += 1
        correct_color_place, correct_color = get_feedback(guess, color_code)

        print(f"Correct color and correct place: {correct_color_place}")
        print(f"Correct color and wrong place: {correct_color}\n")

        if correct_color_place == 4:
            print(f"Congratulations! You've cracked the code in {attempts} attempt(s).")
            print(f"The Correct code is: {''.join(color_code)}")
            break
        elif attempts == 10:
            print(f"Game Over! The correct code was: {''.join(color_code)}")

    if input("Do you want to play again? [Y/N]: ").strip().upper() == "Y":
        play_game()
    else:
        print("Thanks for playing! Hope you enjoyed the game!")

if __name__ == "__main__":
    play_game()
