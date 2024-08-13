
import time
def initializer():
    timestamp= time.strftime('%H:%M:%S')
    hour=int(time.strftime('%H'))
    min=int(time.strftime('%M'))
    name=str(input('''⌚ Welcome to Posh Watch ⌚
Enter your name: '''))

    format=input('''If you want your time in:
24 hours format, type 1
12 hours format, type 2:
''')
    print("\033c")
    return name, hour, min, format

def check_format(name, hour, min, format):
    print("Hi",name)
    try:
        if int(format)==1:
            print(f"Current Time: {hour:02d}:{min:02d}")
        elif int(format)==2:
            if hour>12:
               hour_12= hour-12
               print(f"Current Time: {hour_12:02d}:{min:02d} pm")
            elif hour <=12:
               print(f"Current Time: {hour:02d}:{min:02d} am")
            
    except:
        print("Something went wrong! ❌ Invalid syntax")
    print("Thank You")   

def main():
    name, hour, min, format= initializer()
    check_format(name, hour, min, format)

if __name__== "__main__":
    main()
