def factorial(n): # Calculate the factorial of a non-negative integer n.

    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def get_non_negative_integer(reply):
   
    while True:
        try:
            value = int(input(reply))
            if value < 0:
                print("\033[91mError: Input must be a non-negative integer.\033[0m")
            else:
                return value
        except ValueError:
            print("\033[91mError: Invalid input. Please enter a non-negative integer.\033[0m")

def main():
   
    while True:
        i = input("Enter a number to calculate its factorial (or press Enter to quit): ")
        if i.strip() == "":
            print("Exiting the program.")
            break
        try:
            number = int(i)
            if number < 0:
                print("\033[91mError: Please enter a non-negative integer.\033[0m")
            else:
                print(f"Factorial ({number}!): {factorial(number)}")
        except ValueError:
            print("\033[91mError: Invalid input. Please enter a non-negative integer.\033[0m")

if __name__ == "__main__":
    main()
