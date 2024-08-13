def get_name():
   print("********* Welcome to Beta Calculator *********")
   name=str(input("Enter Your Name: "))
   return name

def check_password(name):
   password= input(f"Hi {name} \nTo ensure that you are not robot, enter the password (hint: 910): ")
   while True:
    
    if int(password)==910:
      print("Access granted")
      break
    else:
      password= int(input("Access denied (hint: 910)"))
      continue

def calculation():
    while True:
     try:
        n1=float(input("Enter the first number:"))
        n2=float(input("Enter the second number:"))

     
        x=int(input('''For addition, type 1
For subtraction, type 2
For multiplication, type 3
For division, type 4: '''))

        if x==1:
          print(f"Answer: {n1} + {n2} =",n1+n2)
        elif x==2:
          print(f"Answer: {n1} - {n2} =",n1-n2)
        elif x==3:
          print(f"Answer: {n1} x {n2} =",n1*n2)
        elif x==4:
          print(f"Answer: {n1} / {n2} =",n1/n2)
        else:
          print("invalid syntax")
     except:
        print("Invalid input")

     check= input("Press Enter to calculate again or Q to Quit: ")
     if check=="":
        continue
     elif check.upper()=="Q":
        break
     else:
        print("Invalid input")
        break
    

def main():
   password= get_name()
   check_password(password)
   calculation()

main()



   


