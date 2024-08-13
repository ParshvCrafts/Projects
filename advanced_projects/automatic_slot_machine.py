
import random
import time

MAIN_LINES = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {"🍇": 5, "🍉": 8, "🍊": 12, "🍎": 15}
symbol_value = {"🍇": 10, "🍉": 5, "🍊": 3, "🍎": 2}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines

def get_symbols(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        for symbol in column:
            all_symbols.remove(symbol)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        credentials = input("Enter card details to make deposit (XXX-XXX): ")
        if len(credentials) != 7:
            print("Enter a valid card number!")
            continue
        else:
            CVV = input("Enter the CVV number (Hint: 123): ")
            if CVV != "123":
                print("Access Denied!")
                continue
            else:
                break
    while True:
        amount = input("Enter your deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("To Play, enter a deposit greater than 0.")
        else:
            print("Enter a valid amount!")

def get_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAIN_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAIN_LINES:
                return lines
            else:
                print(f"Enter a valid number of lines between 1 and {MAIN_LINES}.")
        else:
            print("Enter a valid number of lines.")

def get_bet():
    while True:
        bet = input(f"Enter your bet per line (${MIN_BET}-${MAX_BET}): $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Bet amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Enter a valid bet amount.")

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Insufficient balance. You need ${total_bet - balance} more to play. Current balance: ${balance}")
        else:
            break
    print(f"Betting ${bet} on {lines} lines. Total bet: ${total_bet}")
    
    print("Spinning...")
    time.sleep(1)  # Adding a slight delay to simulate spinning

    slots = get_symbols(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    
    if winnings > 0:
        print(f"🎉 You won ${winnings}! 🎉")
        if winnings_lines:
            print("Winning lines:", ", ".join(map(str, winnings_lines)))
    else:
        print("No winning lines. Better luck next time!")

    return winnings - total_bet

def main():
    print("💎💎💎 Welcome to Diamond Casino! 💎💎💎")
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        action = input("Press Enter to play or Q to quit: ").lower()
        if action == 'q':
            break
        elif action == '':
            balance += spin(balance)
        else:
            print("Invalid input. Try again.")
    print(f"Thanks for playing! You left with ${balance}")

if __name__ == "__main__":
    main()
