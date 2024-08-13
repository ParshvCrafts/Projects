
import string
import random

def generate_password(length, include_letters, include_digits, include_special_chars):
    character_pool = ""
    password = []

    if include_letters:
        character_pool += string.ascii_letters
        password.append(random.choice(string.ascii_letters))

    if include_digits:
        character_pool += string.digits
        password.append(random.choice(string.digits))
        
    if include_special_chars:
        character_pool += string.punctuation
        password.append(random.choice(string.punctuation))

    if len(character_pool) == 0:
        raise ValueError("At least one character set must be selected")

    remaining_length = length - len(password)
    if remaining_length < 0:
        raise ValueError("Password length too short to include required character sets")

    for _ in range(remaining_length):
        password.append(random.choice(character_pool))

    random.shuffle(password)
    return "".join(password)

def main():
    try:
        length = int(input("Enter password length: "))

        print('''Choose character set for password from these: 
        1. Letters
        2. Digits
        3. Special characters
        4. Exit''')

        include_letters = False
        include_digits = False
        include_special_chars = False

        while True:
            choice = int(input("Pick a number: "))
            if choice == 1:
                include_letters = True
            elif choice == 2:
                include_digits = True
            elif choice == 3:
                include_special_chars = True
            elif choice == 4:
                break
            else:
                print("Please pick a valid option!")

        password = generate_password(length, include_letters, include_digits, include_special_chars)
        print("The random password is:", password)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
