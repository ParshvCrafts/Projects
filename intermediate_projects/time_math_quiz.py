
import random
import time
from operator import add, sub, mul

class TimedMathQuiz:
    OPERATORS = {'+': add, '-': sub, '*': mul}
    MIN_OPERAND = 3
    MAX_OPERAND = 12
    TOTAL_PROBLEMS = 10

    def __init__(self):
        self.wrong_attempts = 0
        self.start_time = 0
        self.end_time = 0

    def generate_problem(self):
        left = random.randint(self.MIN_OPERAND, self.MAX_OPERAND)
        right = random.randint(self.MIN_OPERAND, self.MAX_OPERAND)
        operator = random.choice(list(self.OPERATORS.keys()))
        answer = self.OPERATORS[operator](left, right)
        return f"{left} {operator} {right}", answer

    def start_quiz(self):
        input("Get Ready! Press Enter to start:")
        print("---------------")
        self.start_time = time.time()

        for i in range(1, self.TOTAL_PROBLEMS + 1):
            problem, correct_answer = self.generate_problem()
            user_answer = self.get_user_answer(i, problem)

            while user_answer != correct_answer:
                print("Incorrect! Try again.")
                self.wrong_attempts += 1
                user_answer = self.get_user_answer(i, problem)

        self.end_time = time.time()
        self.display_results()

    def get_user_answer(self, problem_number, problem):
        while True:
            try:
                return int(input(f"Problem #{problem_number}: {problem} = "))
            except ValueError:
                print("Invalid input! Please enter a number.")

    def display_results(self):
        total_time = round(self.end_time - self.start_time, 2)
        print("------------------")
        print(f"Nice Work! You finished in {total_time} seconds.")
        print(f"You got {self.wrong_attempts} times wrong answers.")

if __name__ == "__main__":
    quiz = TimedMathQuiz()
    quiz.start_quiz()
