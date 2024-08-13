
import random

max_score = 50
player_name = []

def roll():
    die = ["1", "2", "3", "4", "5", "6"]
    roll = random.choice(die)
    return int(roll)

def display_instructions():
    print("\033c")
    print("\n** PIG Instructions **")
    print("-" * 60)
    print("1. Each player takes turns to roll a die.")
    print("2. On each turn, a player can roll as many times as they like.")
    print("3. The player's turn ends when they choose to stop rolling or roll a 1.")
    print("4. If a player rolls a 1, they lose all points for that turn.")
    print("5. The first player to reach or exceed 50 points wins, but if another player hasn’t rolled yet, they get a chance to beat the score.")
    print("6. The player with the highest score after all turns is the winner.")
    print("-" * 60+ "\n")

while True:
    print("\033c")
    print("Welcome to the PIG Game!")
    if input("Do you need instructions? [Y/N]: ").strip().lower() == "y":
        display_instructions()

    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            for i in range(players):
                name = input(f"Enter the name of Player {i + 1}: ")
                player_name.append(name)
            break
        else:
            print("Players must be between 2 and 4 to play.")
    else:
        print("Invalid input, try again!")

player_score = [0 for _ in range(players)]
max_player_index = None

while True:
    for i in range(players):
        print(f"\n{player_name[i]}, your turn has started!")
        print(f"Your total score is: {player_score[i]}")
        current_score = 0

        while True:
            should_roll = input("\nWould you like to roll? (Y to roll, anything to hold) ").strip().lower()
            if should_roll != "y":
                print(f"{player_name[i]} holds with {current_score} points this turn.")
                break
            value = roll()
            if value == 1:
                print("Oops! You rolled a 1. No points this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
                print(f"Your current turn score is: {current_score}")

        player_score[i] += current_score
        print(f"Your total score is now: {player_score[i]}")

        if player_score[i] >= max_score:
            if max_player_index is None:
                max_player_index = i
                print(f"\n{player_name[i]} has reached the target score! Other players will get a final turn to beat this score.")
            elif i == max_player_index:
                print(f"\n{player_name[max_player_index]} has won the game with a score of {player_score[max_player_index]}!")
                exit()

    if max_player_index is not None:
        print(f"\nFinal round complete! {player_name[max_player_index]} is the winner with a score of {player_score[max_player_index]}!")
        break