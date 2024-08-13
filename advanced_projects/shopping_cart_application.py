import time
def display_cart(cart):
    if not cart:
        print("Your cart is empty")
    else:
        print("****Your Shopping Cart****")
    total_price= 0
    for item in cart:
        print(f"{item["name"]}: ${item["price"]}, quantity: {item["number"]} ")
        total_price += item["price"]* item["number"]
    print(f"Total: ${total_price:.2f}")
    return total_price

def main():
    cart= []
    Clear_and_retrun= "\033c"
    while True:
        print(Clear_and_retrun)
        print("\n*** Welcome to Corny AI Assisstant Shopping Cart ***")
        print("1. Add Item to Cart")
        print("2. View Cart")
        print("3. Remove Item to Cart")
        print("4. Proceed to Buy")
        print("5. Exit")

        choice= input("Enter your choice: ")
        if choice== "1":
            print(Clear_and_retrun)
            item_name= input("Enter item name: ")
            item_price= float(input("Enter item price: "))
            quantity= int(input("Enter the quantiy for the item: "))
            item= {"name": item_name, "price": item_price, "number": quantity}
            cart.append(item)
            print("Item added to the cart")
            bill= display_cart(cart)
            time.sleep(5)

        elif choice=="2":
            print(Clear_and_retrun)
            display_cart(cart)
            time.sleep(5)

        elif choice=="3":
            print(Clear_and_retrun)
            if not cart:
                print("Your cart is already empty")
            else:
                while True:
                   display_cart(cart)
                   item_index= int(input("Enter the item number to remove: ")) -1
                   if 0<= item_index< len(cart):
                      removed_item= cart.pop(item_index)
                      print(f"Removed item: {removed_item["name"]}")
                      break
                   else:
                      print("Enter a valid item to remove\n")
                      continue
            time.sleep(5)

        elif choice== "4":
             print(Clear_and_retrun)
             if not cart:
                 print("Nothing to purchase in your cart. First add item")
                 time.sleep(2)
                 continue
             else:
                 
                 print(f"Your total bill is {bill}")
                 while True:
                     payment=input("Press [1] to pay with Card/ [2] to pay with Cash: ")
                     if payment=="1":
                          while True:
                              credentials= input("Enter card details to make deposit.(XXX-XXX) form: ")
                              if len(credentials)!= 7:
                                 print("Enter a valid card number!")
                                 continue
                              else:
                                CVV= input("Enter the CVV number: (Hint: 123) ")
                                if CVV!= "123":
                                    print("Access Denied!")
                                    continue
                                else:
                                    break

                          amount=input("Enter your withdrawal amount: $")
                          if amount.isdigit():
                            amount=int(amount)
                            if amount>= bill:
                                print(f"${ bill} has been credited from card. Your change ${amount-bill} has been deposited")
                                print("Thank You for your purchase. Visit again")
                                break
                            else:
                                print(f"You don't have enough money to buy. You need ${bill- amount}")
                                continue
                          else:
                            print("Enter valid amount!")
                            continue 
                          
                     elif payment=="2":
                          while True:
                              value= int(input("Enter the Note value: "))
                              cash= int(input("Enter the number of notes: "))
                              if cash*value>= bill:
                                print(f"Your change ${(cash*value)-bill} has been dispensed")
                                print("Thank You for your purchase. Visit again")
                                break
                              else:
                                print(f"You don't have enough money to buy. You need ${bill- (cash*value)} cash")
                                continue
                     cart=[]
                     time.sleep(2)
                     break

        elif choice=="5":
            print(Clear_and_retrun)
            print("Exited the application")
            time.sleep(2)
            break

        else:
            print("Invalid choice. Please select a valid option")
            continue

if __name__== "__main__":
    main()
