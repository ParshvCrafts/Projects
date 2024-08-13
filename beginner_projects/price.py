def main():
    try:
       name=str(input("Welcome to Corny(AI Assistant), Enter your name: "))
       budget=int(input("Please enter your budget($): "))
       milk=int(input('''Current Milk price: $3 per gallon\nPlease enter your quantity: '''))
       juice=int(input('''Current Juice price: $5 per container\nPlease enter your quantity: '''))
       print(f"Hi {name}, let's check what you got")
       price=3*milk+5*juice
       save= budget-price
       if save>0:
         print("Yes you can buy it")
         print("Total:$",price)
         print("You can save $", save,"good job") 
         charity=int(input("Would you like to donate to charity? Enter the amount: "))
         if charity>0:
            if charity>=budget-save:
               print(f"Thank You for donating ${charity} for good cause.")
            else:
               print("You cannot donate more than your savings.")
       else:
         print(f"Your expense is over the budget by ${price-budget}\nSorry you cannot buy it")
    except:
       print("Something went wrong! Invalid Input")

if __name__== "__main__":
   main()
    
