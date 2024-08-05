import turtle
import time
import random

WIDTH, HEIGHT= 500, 500
COLORS= ["red","green","orange","black","blue", "pink","brown", "cyan"]

def number_racers():
    racers=0
    while True:
        racers=input("Enter the number of racers (2-8): ")
        if racers.isdigit():
            if 2<= int(racers) <= 8:
                break
            else: 
                print("Numbers not in range (2-8):")
        else:
            print("Enter a valid number to play")
            continue

    return racers
def bet_turtle(color):
    while True:
        guess= input(f"Bet on the winner of the Turtle. Options: {color} ")
        if guess in color:
            break
        else:
            print("Enter a valid bet!")
            continue
    return guess

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

def create_turtles(colors):
    turtles=[]
    spacing= WIDTH/ (len(colors)+1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH/2+(i+1)*spacing, -HEIGHT/2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles= create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance=random.randrange(1, 20)
            racer.forward(distance)
            x, y=racer.pos()
            if y>= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]
            
def check_bet(guess, winner):
    if winner== guess:
        print("Hurray!, you guessed the correct winner.")
    else:
        print("Sorry, you lost your bet")

def main():
    print("*****🐢 Welcome to Turtle Racing Game 🐢*****")
    racers=number_racers()
    random.shuffle(COLORS)
    color= COLORS[:int(racers)]
    guess= bet_turtle(color)
    init_turtle()
    winner= race(color)
    print(f"The winner is {winner.title()} 🐢 turtle")
    check_bet(guess, winner)
    time.sleep(10)

if __name__== "__main__":
    main()