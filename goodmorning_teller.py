import time
def intializer():
    name=str(input('''***⌚ Welcome to Posh Watch ⌚***
Enter your name: '''))
    print("\033c")
    timestamp= time.strftime('%H:%M:%S')
    hour=int(time.strftime('%H'))
    min=int(time.strftime('%M'))
    return name, hour, min


def check_timings(name, hour, min):
    if 12>hour>6:
        print(f"Good Morning, {name}\nTime: {hour}:{min}")

    elif hour==12:
        if min==0:
            print(f"Good Noon, {name}\nTime: {hour}:{min}")

    elif 16>=hour>=12:
        print(f"Good AfterNoon, {name}\nTime: {hour}:{min}")

    elif 20>=hour>16:
        print(f"Good Evening, {name}\nTime: {hour}:{min}")

    elif 24>=hour>20:
        print(f"Good Night, {name}\nTime: {hour}:{min}")

    elif hour==0:
        if min==0:
            print(f"Good Mid-Night, {name}\nTime: {hour}:{min}")
    
    elif 6>=hour>=0:
        print(f"Good Night, {name}\nTime: {hour}:{min}")

def main():
    name, hour, min= intializer()
    check_timings(name, hour, min)

if __name__=="__main__":
    main()