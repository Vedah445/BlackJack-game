from values import cards, points
import random
from logo import logo

def get_input():
    print(f"computer has: {computer[0]}")
    print(f"you have: {user} \t total = {sum(user)}")        
    print("\n \n")

    if sum(user) == 21:
        display("win")
    chooice = input("hit or stand: ")
    deal(chooice)
    
def add_computer():
    computer.pop()
    computer.append(random.choice(cards))
    if sum(computer) > 21:
      add_computer()
    else:
        return
    
def deal(choice):
    #hit condition
    if choice == "hit":
        a = random.choice(cards)
        if a == 11 and sum(user) > 21:
            user.append(1)
        else:
            user.append(a)
        print("\n")
        if sum(user) > 21: 
            display("lose1")
        
        else:
            get_input()
    
    #stand condition
    elif choice == "stand":
        print("\n ")
        if sum(computer) < 17:
            print(f"computer has {computer}\t total = {sum(computer)}")
            computer.append(random.choice(cards))
            if sum(computer) > 21:
                add_computer()
            print(f"after adding more,computer has {computer}\t total = {sum(computer)}")
           
        print("\n")

        
        if sum(user) > sum(computer):
            display("win")
        elif sum(user) < sum(computer):
            display("lose2")
        else:
            print("draw")
        
def display(st):
    global wager
    global points
    print(f"computer has {computer}\t total = {sum(computer)}")
    print(f"you have {user} \t total = {sum(user)}")
    print("\n \n")
    if st == "lose1":
        print("YOU LOST!!!!! ")
        points -= wager
        print("you lost because you had too many numbers")
        
    elif st == "lose2":
        print("YOU LOST!!!!! ")
        points -= wager
        print("computer had more numbers than you")
    elif st == "win":
        print("YOU WIN CONGRATS!!!!! ")
        points += wager
        print("congrats on your win")
            
    inp = input("play again? ")
    if inp == "yes":
        print("you have: ", points)
        wager = int(input("how much do you wager? "))
        get_input()
        

computer = [random.choice(cards), random.choice(cards)]
user = [random.choice(cards), random.choice(cards)]

print(logo)

print("you have: ", points)


#ask the user to hit or stand
wager = int(input("how much do you wager? "))

get_input()






