def computepay(hours, rate):
    
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay

def get_input(prompt):
    
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("\033[91mError: Input must be a non-negative number.\033[0m")
                continue
            return value
        except ValueError:
            print("\033[91mError: Invalid input. Please enter a numeric value.\033[0m")

def main():
    
    print("Pay Calculator")
    hours = get_input("Enter Hours worked : ")
    rate = get_input("Enter Rate per Hour: ")
    pay = computepay(hours, rate)
    print(f"Your Weekly Pay is: ${pay:.2f}")

if __name__ == "__main__":
    main()
