from values import cards
import random
from logo import logo

def display(st):
    
    print("\n \n")
    if st == "lose1":
        print("YOU LOST!!!!! ")
        print("you lost because you had too many numbers")
        print(f"computer has {computer}\t total = {sum(computer)}")
        print(f"you have {user} \t total = {sum(user)}")
    elif st == "lose2":
        print("YOU LOST!!!!! ")
        print("computer had more numbers than you")
        print(f"computer has {computer}\t total = {sum(computer)}")
        print(f"you have {user} \t total = {sum(user)}")
    elif st == "win":
        print("YOU WIN CONGRATS!!!!! ")

        print("congrats on your win")
        print(f"computer has {computer}\t total = {sum(computer)}")
        print(f"you have {user} \t total = {sum(user)}")
    
        
        

def get_input():
    chooice = input("hit or stand: ")
    deal(chooice)
    
    
def deal(choice):
    #hit condition
    if choice == "hit":
        if random.choice(cards) == 11 and sum(user) > 21:
            user.append(1)
        else:
            user.append(random.choice(cards))
        print("\n")
        print(f"computer has {computer[0]}")
        print(f"you have {user} \t total = {sum(user)}")
        if sum(user) > 21: 
            display("lose1")
        else:
            get_input()
    
    #stand condition
    elif choice == "stand":
        print(f"computer has {computer}\t total = {sum(computer)}")
        if sum(computer) < 17:
            computer.append(random.choice(cards))
            print(f"after adding more,computer has {computer}\t total = {sum(computer)}")
        
        print(f"you have {user} \t total = {sum(user)}")        
        print("\n \n")

        
        if sum(user) > sum(computer):
            display("win")
        elif sum(user) < sum(computer):
            display("lose2")
        else:
            print("draw")
        
        

computer = [random.choice(cards), random.choice(cards)]
user = [random.choice(cards), random.choice(cards)]

print(logo)

#printing user's cards and one of computer's cards
print(f"computer has: {computer[0]}")
print(f"you have: {user} \t total = {sum(user)}")        
print("\n \n")


#ask the user to hit or stand
get_input()






