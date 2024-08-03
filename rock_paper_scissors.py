import random

def get_user_choice():
    while True:
        user_input = input("Enter a choice (rock, paper, scissors) or Q to quit: ").lower()
        if user_input == "q":
            return None
        if user_input not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please enter rock, paper, or scissors.")
        else:
            return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def print_scores(user_score, computer_score):
    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")

def main():
    user_score = 0
    computer_score = 0
    game_count = 0
    user_wins = 0
    computer_wins = 0
    ties = 0
    
    print("Welcome to the Rock, Paper, Scissors Game!")
    
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            break
        
        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
            ties += 1
        elif winner == "user":
            print("You win!")
            user_score += 1
            user_wins += 1
        else:
            print("Computer wins!")
            computer_score += 1
            computer_wins += 1
        
        game_count += 1
        print_scores(user_score, computer_score)
    
    print("\nGame Over!")
    print(f"Total games played: {game_count}")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties: {ties}")

if __name__ == "__main__":
    main()
