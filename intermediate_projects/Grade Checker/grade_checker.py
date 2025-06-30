"""
simple_grader.py
- Grade a single score or a list of scores stored in a CSV file.
- Gives letter grades, percentages, and basic class statistics.

CSV format (with header):
hours,scores

"""

import csv
import statistics as stats
from pathlib import Path
import time


def get_letter(score: float, total: float) -> str:
    prop = score / total
    if prop >= 0.90:
        return "A"
    elif prop >= 0.80:
        return "B"
    elif prop >= 0.70:
        return "C"
    elif prop >= 0.60:
        return "D"
    else:
        return "F"


def grade_single() -> None:
    try:
        score = float(input("Enter your score: "))
        total = float(input("Enter the total points: "))
        print("Calculating......")
        time.sleep(3)
        if 0 <= score <= total:
            letter = get_letter(score, total)
            pct = round(score / total * 100, 2)
            print(f"\nScore: {score} / {total} ({pct}%)  → Grade {letter}\n")
            time.sleep(3)
        else:
            print("Error: Score must be between 0 and the total points.")
    except ValueError:
        print("Error: Please enter numeric values only.")


def grade_class(csv_path: Path, total: float) -> None:
    # reading CSV
    Hours, Scores, letters = [], [], []
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            Scores.append(float(row["Scores"]))
            Hours.append(float(row["Hours"]))

    #grading everyone
    for s in Scores:
        letters.append(get_letter(s, total))
        
    if 0 <= max(Scores) <= total:   

        for n, s, ltr in zip(Hours, Scores, letters):
            pct = round(s / total * 100, 2)
            print(f"{n:15} {s:>6}/{total}  {pct:6.2f}%  {ltr}")

        # statistics
        avg = stats.mean(Scores)
        med = stats.median(Scores)
        high, low = max(Scores), min(Scores)
        avg_hours= stats.mean(Hours)
    
        print("\n=== Class Stats ===")
        print(f"Students : {len(Scores)}")
        print(f"Average  : {avg:.2f}")
        print(f"Median   : {med:.2f}")
        print(f"High | Low : {high} | {low}")
        print(f"Average Hours studied: {round(avg_hours, 2)} hours")
        letter = get_letter(avg, total)
        pct = round(avg / total * 100, 2)
        print(f"\nOverall score for the class: {avg} %  → Grade {letter}\n")
        time.sleep(3)
    
    else:
        
        print("Error: Score must be between 0 and the total points.")
    

def main():
    print("Smart Grader\n============")
    print("1) Grade a single score")
    print("2) Grade a class from CSV file")
    choice = input("Select an option (1 or 2): ")

    if choice == "1":
        grade_single()
    elif choice == "2":
        path_str = input("CSV file path: ").strip()
        total = float(input("Total points for the test: "))
        print("Calculating.....")
        time.sleep(3)
        grade_class(Path(path_str), total)
    else:
        print("Invalid choice. Goodbye.")


if __name__ == "__main__":
    main()
