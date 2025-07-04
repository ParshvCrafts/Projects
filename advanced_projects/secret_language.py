
# import time
# import string
# import random

# def get_script():
#     print("\033c")
#     print("🔠📩  Welcome to Secret Code Language Simulator 📩🔤")
#     while True:
#         try:
#             prompt= int(input("Enter 1 to Encrypt a message / 2 to Decrypt a message / 3 to Quit: "))
#             if prompt in [1, 2, 3]:
#                 print("\033c")
#                 if prompt== 1:
#                     encrypt= input("Enter the message to encrypt into a secret code: ")
#                     if len(encrypt) == 0:
#                         print("Enter valid message to encrypt")
#                         continue
#                     else:
#                         encrypted_message=encrypt_message(encrypt)
#                         print(f"Here is your encrypted code: {encrypted_message}\n")
#                         continue

#                 elif prompt == 2:
#                     decrypt= input("Enter the message to decrypt into a secret code: ")
#                     if len(decrypt) == 0:
#                         print("Enter valid message to encrypt")
#                         continue
#                     else:
#                         decrypted_message = decrypt_message(decrypt)
#                         print(f"Here is your decrypted message: {decrypted_message}\n")
#                         time.sleep(5)
#                         continue

#                 elif prompt== 3:
#                     print("Leaving the simulator!")
#                     time.sleep(2)
#                     break
#         except ValueError:
#             print("Enter a valid input (1, 2, or 3) !")
#             continue

# def encrypt_message(encrypt):
#     words= encrypt.split()
#     encrypted_words = []

#     for word in words:
#         if len(word) >= 3:
#             # Rotate the first character to the end
#             word = word[1:] + word[0]
#             # Add random letters at the beginning and end
#             prefix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
#             suffix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
#             encrypted_word = prefix + word + suffix
#         else:
#             # Reverse the word for words with length less than 3
#             encrypted_word = word[::-1]
        
#         encrypted_words.append(encrypted_word)
    
#     return ' '.join(encrypted_words)
        
# def decrypt_message(encrypted_message):
#     words = encrypted_message.split()
#     decrypted_words = []

#     for word in words:
#         if len(word) > 6:
#             # Remove the first 3 and last 3 random letters
#             core_word = word[3:-3]
#             # Rotate the last character to the beginning
#             decrypted_word = core_word[-1] + core_word[:-1]
#         else:
#             # Reverse the word back for words with length less than 3
#             decrypted_word = word[::-1]
        
#         decrypted_words.append(decrypted_word)
    
#     return ' '.join(decrypted_words)
        
# if __name__ == "__main__":
#     get_script()


"""
Secret‑Code Simulator 2.1
─────────────────────────
•  Choose Encrypt / Decrypt
•  Work with plain text or an entire .txt file
•  Optional save‑to‑file (default names: encrypted.txt / decrypted.txt)
─────────────────────────
Author : Parshv Patel  │  July 2025
"""

import random
import string
import time
from pathlib import Path

LETTERS = string.ascii_letters


# ────────────────  CIPHER LOGIC  ──────────────── #
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
        return input("\nEnter / paste your text ▶ ")
    if choice == "2":
        path = Path(input("Path to .txt ▶ ").strip())
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
        name = input(f"Filename [default: {default_name}] ▶ ").strip() or default_name
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
                    "\n1) Encrypt\n2) Decrypt\n3) Quit\n --> "
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
