
def main():
  print('''Welcome to ***"Even Odd Tester"***''')
  Clear_and_retrun= "\033c" # Escape sequence character to return cursor to home position to print over
  while True:
    n1=int(input("Enter the number: "))
    try:
      n2=float(n1/2)-int(n1/2)
    except:
      n2=-1
   
    if n2==0:
       print(f"{n1} is a Even number")
    else:
       print(f"{n1} is a Odd number")
    

    check= input("Press enter to continue or Q to Quit: ")
    if check=="":
      print(Clear_and_retrun)
      continue
    elif check.upper()=="Q":
      break
    else:
      print("Invalid input")
      break

if __name__== "__main__":
  main()


