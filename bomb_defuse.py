import random
import time

def main():
    print("*** Defuse the Bomb ***")
    print("You are a Bomb Defuser. Guess the correct password to defuse {0-9}. If you fail, you have 5 seconds to run away")
    code= random.randint(0, 9)
    enter=int(input(f"Enter correct code: "))
    
    Clear_and_retrun= "\033c"

    if enter==code:
       print(Clear_and_retrun)
       print("Congratulations, bomb successfully defused! :>")
    else:
       n=5
       while n>-1:
         print(Clear_and_retrun)
         print(n)
         time.sleep(1)
         n=n-1
       print("💥💥💥, you lost")

main()
