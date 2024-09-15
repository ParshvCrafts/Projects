
import curses
from curses import wrapper
import time
import random
import os

EASY_TEXT_FILE = "easy_text.txt"
MEDIUM_TEXT_FILE = "medium_text.txt"
HARD_TEXT_FILE = "hard_text.txt"
LEADERBOARD_FILE = "leaderboard.txt"

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Test!", curses.A_BOLD)
    stdscr.addstr("\nSelect Difficulty Level:", curses.A_UNDERLINE)
    stdscr.addstr("\n1. Easy")
    stdscr.addstr("\n2. Medium")
    stdscr.addstr("\n3. Hard")
    stdscr.addstr("\nPress the number corresponding to your choice. ")
    stdscr.refresh()

def choose_difficulty(stdscr):
    while True:
        try:
            key = stdscr.getkey()
            if key == '1':
                return EASY_TEXT_FILE
            elif key == '2':
                return MEDIUM_TEXT_FILE
            elif key == '3':
                return HARD_TEXT_FILE
            else:
                stdscr.addstr(7, 0, "Invalid selection. Press 1, 2, or 3.")
                stdscr.refresh()
        except:
            continue

def display_text(stdscr, target_text, current_text, wpm=0, accuracy=100):
    stdscr.addstr(0, 0, target_text, curses.color_pair(3))
    stdscr.addstr(2, 0, f"WPM: {wpm} | Accuracy: {accuracy:.2f}%", curses.color_pair(3))

    for i, char in enumerate(current_text):
        correct_char = target_text[i]
        if char == correct_char:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        else:
            stdscr.addstr(0, i, char, curses.color_pair(2))

    stdscr.refresh()

def load_text(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def calculate_accuracy(target_text, current_text):
    correct_chars = sum(1 for i, char in enumerate(current_text) if char == target_text[i])
    return (correct_chars / len(target_text)) * 100 if len(target_text) > 0 else 0

def update_leaderboard(wpm, accuracy):
    leaderboard = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            leaderboard = [line.strip().split(",") for line in file.readlines()]

    leaderboard.append([str(wpm), f"{accuracy:.2f}"])
    leaderboard.sort(key=lambda x: int(x[0]), reverse=True)

    with open(LEADERBOARD_FILE, "w") as file:
        for entry in leaderboard[:5]:  # Only store top 5 scores
            file.write(",".join(entry) + "\n")

def display_leaderboard(stdscr):
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            leaderboard = [line.strip().split(",") for line in file.readlines()]

        stdscr.addstr(5, 0, "\nLeaderboard:", curses.A_BOLD)
        for i, (wpm, accuracy) in enumerate(leaderboard):
            stdscr.addstr(6 + i, 0, f"{i+1}. WPM: {wpm}, Accuracy: {accuracy}%")
        stdscr.refresh()

def wpm_test(stdscr, filename):
    target_text = load_text(filename)
    current_text = []
    wpm = 0
    accuracy = 100
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_passed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_passed / 60)) / 5)
        accuracy = calculate_accuracy(target_text, current_text)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm, accuracy)

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # ESC key to quit
            break
        elif key in ("KEY_BACKSPACE", "\b", "\x7f"):  # Handle backspace
            if current_text:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    return wpm, accuracy

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while True:
        start_screen(stdscr)
        filename = choose_difficulty(stdscr)

        stdscr.clear()
        stdscr.addstr("Get ready to start typing...", curses.A_BOLD)
        stdscr.refresh()
        time.sleep(1)

        wpm, accuracy = wpm_test(stdscr, filename)
        update_leaderboard(wpm, accuracy)

        stdscr.clear()
        stdscr.addstr(0, 0, f"Test Completed! Your WPM: {wpm}, Accuracy: {accuracy:.2f}%")
        display_leaderboard(stdscr)
        stdscr.addstr(10, 0, "\nPress any key to continue or ESC to quit.")
        stdscr.refresh()

        key = stdscr.getkey()
        if ord(key) == 27:  # ESC key to quit
            break

wrapper(main)
