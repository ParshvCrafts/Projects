def fib(n): # Generate a list containing the first n Fibonacci numbers.

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    a = [0, 1]
    for i in range(2, n):
        a.append(a[i - 1] + a[i - 2])
    return a

def get_positive_integer(prompt):
    
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("\033[91mError: Input must be a positive integer.\033[0m")
            else:
                return value
        except ValueError:
            print("\033[91mError: Invalid input. Please enter a positive integer.\033[0m")

def main():
    
    n = get_positive_integer("Enter the number of Fibonacci numbers to generate: ")
    fibonacci_sequence = fib(n)
    print(f"The first {n} Fibonacci numbers are: {fibonacci_sequence}")

if __name__ == "__main__":
    main()
