"""
A slightly upgraded Hangman game which is beginner-friendly, but with
- categories (Animals, Food, Tech)
- hint option (reveals one random letter, costs one try)
- simple score board that tracks wins/losses
- word list can be expanded via a plain-text file (one word per line)
"""

from pathlib import Path
from typing import Dict, List, Tuple
import random
import sys
import time

BUILT_IN: Dict[str, List[str]] = {
    "ANIMALS": ["panther", "dolphin", "toucan", "giraffe", "otter"],
    "FOOD":    ["lasagna", "avocado", "cinnamon", "pancake", "blueberry"],
    "TECH":    ["python", "algorithm", "quantum", "database", "firewall"],
}

# default external list path (change if you like)
DEFAULT_EXTRA_PATH = Path(r"C:\Users\p1a2r\OneDrive\Desktop\Git Hub Projects\hangman_words.txt")

def ask_source() -> str:
    """Return 'BUILTIN' or absolute path to custom list (guaranteed to exist)."""
    print("\nWord list options:")
    print("  1) Built‑in categories")
    print("  2) Use my own text‑file list")
    choice = input("Choose 1 or 2:  ").strip()
    if choice == "1":
        return "BUILTIN"
    if choice == "2":
        path = input(f"Path to your .txt file [{DEFAULT_EXTRA_PATH}]: ").strip()
        path = path or str(DEFAULT_EXTRA_PATH)
        if not Path(path).is_file():
            print(f"✖  File not found: {path}")
            sys.exit(1)
        return path
    print("✖  Invalid choice.")
    sys.exit(1)

def load_external(path: Path) -> List[str]:
    """Read one‑word‑per‑line list; keep only alphabetic words."""
    with open(path, 'r', encoding="utf‑8") as f:
        words = [w.strip().lower() for w in f if w.strip().isalpha()]
    if not words:
        print("✖  No valid words in file.")
        sys.exit(1)
    return words

def choose_word(source_token: str) -> Tuple[str, str]:
    """Return (word, category)."""
    if source_token == "BUILTIN":
        category = random.choice(list(BUILT_IN.keys()))
        word = random.choice(BUILT_IN[category])
    else:  # custom list
        category = "CUSTOM"
        word = random.choice(load_external(Path(source_token)))
    return word.upper(), category

HANGMAN_PICS = [  # 6 → 0 tries left
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     / \
       -""",
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     /
       -""",
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |
       -""",
    r"""
       --------
       |      |
       |      O
       |     \|
       |      |
       |
       -""",
    r"""
       --------
       |      |
       |      O
       |      |
       |      |
       |
       -""",
    r"""
       --------
       |      |
       |      O
       |
       |
       |
       -""",
    r"""
       --------
       |      |
       |
       |
       |
       |
       -""",
]

MAX_TRIES = len(HANGMAN_PICS) - 1
score = {"Wins": 0, "Losses": 0}

def reveal_hint(word: str, current: str, tries: int) -> Tuple[str, int]:
    hidden = [i for i, ch in enumerate(word) if current[i] == "_"]
    if hidden and tries:
        idx = random.choice(hidden)
        current = current[:idx] + word[idx] + current[idx + 1 :]
        tries -= 1
        print(f"Hint used! letter '{word[idx]}' revealed (‑1 try).\n")
        time.sleep(2)
    return current, tries

def play_round(source_token: str) -> None:
    word, cat = choose_word(source_token)
    display = "_" * len(word)
    guessed_letters, guessed_words = set(), set()
    tries = MAX_TRIES

    while tries and "_" in display:
        print("\033c")
        print(HANGMAN_PICS[MAX_TRIES - tries])
        print(f"Category: {cat}")
        print(f"Word: {' '.join(display)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
        print(f"Guessed words: {', '.join(sorted(guessed_words)) if guessed_words else '-'}")  
        print(f"Tries left: {tries}")
        guess = input("Guess a letter/word or type 'hint': ").strip().upper()

        # Handle hint
        if guess == "HINT":
            display, tries = reveal_hint(word, display, tries)
            continue

        # Letter guess
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("⚠ You already guessed that letter.\n")
                time.sleep(3)
            elif guess in word:
                guessed_letters.add(guess)
                display = "".join(guess if word[i] == guess else ch for i, ch in enumerate(display))
            else:
                guessed_letters.add(guess)
                tries -= 1
                print("✖  Letter not in word.\n")
                time.sleep(3)
            continue

        # Word guess
        if len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("⚠  Already tried that word.\n")
                time.sleep(3)
            elif guess == word:
                display = word
            else:
                guessed_words.add(guess)
                tries -= 1
                print("✖  Incorrect word.\n")
                time.sleep(3)
            continue

        print("Invalid input.\n")
        time.sleep(3)

    # Round result
    if "_" not in display:
        score["Wins"] += 1
        print(f"\n🎉 Congratulations!! The word was: {word}.")
    else:
        score["Losses"] += 1
        print(HANGMAN_PICS[0])
        print(f"💀 Out of tries. The word was: {word}.")

def main() -> None:
    print("\033c")
    print("=== Welcome to Hangman ===")
    source = ask_source()
    while True:
        play_round(source)
        print(f"Score →  Wins: {score['Wins']}  |  Losses: {score['Losses']}")
        if input("Play again? (Y/N): ").strip().upper() != "Y":
            print("\033c")
            break
    print("Thanks for playing! Final Score:", score)

if __name__ == "__main__":
    main()


