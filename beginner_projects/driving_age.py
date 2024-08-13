
name=str(input('''*** Welcome To DMV ***
Please enter your legal full name: '''))
age=int(input("Please enter your current age: "))
print("Hi,",name.title())

if age>18:
     print("You are eligible for a driving license")
     
elif age==18:
     print("You need to have a guardian with you for a driving license")
     
else:
     print("Sorry, you are not eligible for driving license")
     print("You can have your license after",18-age,"years")

