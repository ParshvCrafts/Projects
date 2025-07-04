"""
Secret‑Code Simulator 
Author : Parshv Patel  │  July 2025
"""

import random
import string
import time
from pathlib import Path

LETTERS = string.ascii_letters

def encrypt_message(msg: str) -> str:
    result = []
    for word in msg.split():
        if len(word) >= 3:
            rotated = word[1:] + word[0]
            prefix = "".join(random.choice(LETTERS) for _ in range(3))
            suffix = "".join(random.choice(LETTERS) for _ in range(3))
            result.append(prefix + rotated + suffix)
        else:
            result.append(word[::-1])
    return " ".join(result)


def decrypt_message(msg: str) -> str:
    result = []
    for word in msg.split():
        if len(word) > 6:
            core = word[3:-3]
            result.append(core[-1] + core[:-1])
        else:
            result.append(word[::-1])
    return " ".join(result)

def read_source(prompt_msg: str) -> str:
    """Let user paste text OR give a path to a .txt file."""
    choice = input(f"{prompt_msg}\n1) Type/Paste\n2) Load .txt file\n▶ ").strip()
    if choice == "1":
        return input("\nEnter / paste your text:  ")
    if choice == "2":
        path = Path(input("Path to .txt:  ").strip())
        try:
            return path.read_text(encoding="utf‑8")
        except Exception as e:
            print(f"⚠️  Could not read file: {e}")
            return read_source(prompt_msg)
    print("⚠️  Invalid choice.")
    return read_source(prompt_msg)


def handle_output(result: str, default_name: str) -> None:
    """Ask whether to display or write to file."""
    choice = input("\n1) Print on screen\n2) Save to file\n▶ ").strip()
    if choice == "1":
        print("\n────────  RESULT  ────────\n")
        print(result)
        
    elif choice == "2":
        name = input(f"Filename [default: {default_name}] : ").strip() or default_name
        Path(name).write_text(result, encoding="utf‑8")
        print(f"✓  Saved as '{name}'")
    else:
        print("⚠️  Invalid choice; printing instead.\n")
        print(result)

def main() -> None:
    print("\033c") 
    print("📩  Secret‑Code Language Simulator  📩")

    while True:
        try:
            mode = int(
                input(
                    "\n1) Encrypt\n2) Decrypt\n3) Quit\n -> "
                ).strip()
            )
        except ValueError:
            print("⚠️  Enter 1, 2, or 3.")
            continue

        if mode == 3:
            print("\nGood‑bye!")
            time.sleep(1)
            break

        if mode not in (1, 2):
            print("⚠️  Invalid choice.")
            continue
        
        print("\n")
        source_text = read_source(
            "Choose input method for your message/file"
        )
        if not source_text.strip():
            print("⚠️  Empty input. Try again.")
            continue

        if mode == 1:
            result = encrypt_message(source_text)
            handle_output(result, "encrypted.txt")
        else:
            result = decrypt_message(source_text)
            handle_output(result, "decrypted.txt")


if __name__ == "__main__":
    main()
