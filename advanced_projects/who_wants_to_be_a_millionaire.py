
import random
import time
def get_questions():
    questions = [
    ["What color is the sky on a clear day?",
     "Green", "Blue", "Red", "Yellow", "2"],
    
    ["What is the capital of France?",
     "Berlin", "Madrid", "Paris", "Rome", "3"],
    
    ["Which fruit is known for having seeds on the outside?",
     "Apple", "Banana", "Strawberry", "Orange", "3"],
    
    ["How many continents are there on Earth?",
     "Five", "Six", "Seven", "Eight", "3"],
    
    ["What is the largest planet in our solar system?",
     "Earth", "Mars", "Jupiter", "Saturn", "3"],
    
    ["What is the chemical symbol for water?",
     "HO", "H2O", "O2", "CO2", "2"],
    
    ["Who wrote 'Hamlet'?",
     "Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain", "3"],
    
    ["What is the smallest prime number?",
     "1", "2", "3", "5", "2"],
    
    ["Which element has the atomic number 1?",
     "Oxygen", "Helium", "Hydrogen", "Carbon", "3"],
    
    ["In which year did the Titanic sink?",
     "1905", "1912", "1920", "1930", "2"],
    
    ["Who painted the Mona Lisa?",
     "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "3"],
    
    ["What is the square root of 144?",
     "10", "11", "12", "13", "3"],
    
    ["Who discovered penicillin?",
     "Marie Curie", "Alexander Fleming", "Isaac Newton", "Albert Einstein", "2"],
    
    ["What is the hardest natural substance on Earth?",
     "Gold", "Iron", "Diamond", "Platinum", "3"],
    
    ["Which gas is most abundant in the Earth's atmosphere?",
     "Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen", "4"]
    ]
    money= [ 100, 200, 300, 500, 1000, 2000, 5000, 7000, 10000, 30000, 50000,
100000, 500000, 700000, 1000000]
    return questions, money

def main():
    questions, money= get_questions()
    print("\033c")
    print("💵💰🪙  Welcome to Who Wants to be a Millionaire 🪙💰💵")
    print(f"""Rules: You get a Question with 4 options, one of which is correct. You need to answer the correct option in (1-4) format.
Each round will be played for a specific amount with the following sequence: {money}
After each question, you will be given a choice to either continue and risk your amount with wrong answer or Quit and take the amount.
You will get 3 life lives, with each eliminating 2 wrong options. Use them Wisely!
If you get a question wrong than 50% of the amount will be deducted and given back to you.\n""")

    action=input("Once read the instruction, Press Enter to continue: ")
    life= 3
    amount=0
    if action=="":
        for level, content in enumerate(questions):
            while True:
                print("\033c")
                print(f"Question for $. {money[level]}")
                
                print(f"Q {level+1}: {content[0]}")
                print(f"1. {content[1]}")
                print(f"2. {content[2]}")
                print(f"3. {content[3]}") 
                print(f"4. {content[4]}")
                reply = input('Enter your answer(1-4)' + (', or Press "L" to use life line: ' if life > 0 else ': '))
                if reply == content[-1]:
                    print(f"Correct answer, you have won $ {money[level]}")
                    amount= money[level]
                    if amount== money[-1]:
                        print("🎆🥳🎉 Congratulation, You Won! Now you are a Millionaire! Your wit proved valuable 🎆🥳🎉")
                        time.sleep(3)
                        break
                    time.sleep(3)
                    ask= input('Do you want to continue and earn more money? Press "y" to continue or any to not: ')                
                    if ask.upper()=="Y":
                        break
                    else:
                        print(f"Congraulations! Your take away money is {amount}")
                        return
                elif reply.upper()=="L" and life>0:
                
                    life+= -1
                    print("\033c")
                    print(f"You have now {life} lifes left")
                    options= [content[1], content[2], content[3], content[4]]
                    options.remove(content[int(content[-1])])
                    option=random.choice(options)
                    life_list= [option, content[int(content[-1])]]
                    random.shuffle(life_list)

                    print(f"Q {level+1}: {content[0]}")
                    print(f"1. {life_list[0]}")
                    print(f"2. {life_list[1]}")
                    reply= int(input('Enter your answer(1-2): '))
                    answer=  life_list.index(content[int(content[-1])])
                    if reply == answer +1:
                        print(f"Correct answer, you have won $ {money[level]}")
                        amount= money[level]
                        if amount== money[-1]:
                            print("🎆🥳🎉 Congratulation, You Won! Now you are a Millionaire! Your wit proved valuable 🎆🥳🎉")
                            time.sleep(3)
                            break
                        time.sleep(3)
                        ask= input('Do you want to continue and earn more money? Press "y" to continue or any to not: ')                
                        if ask.upper()=="Y":
                            break
                        else:
                            print(f"Congraulations! Your take away money is {amount}")
                            return
                    else:
                        print(f"Wrong answer! the correct answer was option {answer+1} ({content[int(content[-1])]})")
                        amount= (amount*50)/100
                        time.sleep(5)
                        print(f"Congraulations! Your take away money is {amount}")
                        return

                elif reply.upper() == "L" and life == 0:
                    print("You don't have any life lines left")
                    time.sleep(2)

                else:
                    print(f"Wrong answer! the correct answer was option {content[-1]} ({content[int(content[-1])]})")
                    amount= (amount*50)/100
                    time.sleep(5)
                    print(f"Congraulations! Your take away money is {amount}")
                    return

        
    else:
        print("Leaving the Game. Thank you for your interest")
        time.sleep(3)
         

if __name__== "__main__":
    main()  

