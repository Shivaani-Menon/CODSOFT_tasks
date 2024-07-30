import random

class rps():

    def game(self):
        elements=['rock','paper','scissors']
        u=[]
        c=[]
        user_score, comp_score=0,0

        while True:
            comp=random.choice(elements)
            user=input("Make your choice [Rock, Paper, Scissors]: ").lower()
            if user not in elements:
                print("ERROR: Enter appropriate choice [Rock, Paper, Scissors]")
        
            if user == comp:
                print("User: {} VS Computer: {}. It's a TIE!".format(user,comp))
                u.append(1)
                c.append(1)
            elif user == "rock":
                if comp == "paper":
                    print("User: {} VS Computer: {}. User LOSES.".format(user,comp))
                    u.append(0)
                    c.append(1)
                else:
                    print("User: {} VS Computer: {}. User WINS!".format(user,comp))
                    u.append(1)
                    c.append(0)
            elif user == "paper":
                if comp == "rock":
                    print("User: {} VS Computer: {}. User WINS!".format(user,comp))
                    u.append(1)
                    c.append(0)
                else:
                    print("User: {} VS Computer: {}. User LOSES.".format(user,comp))
                    u.append(0)
                    c.append(1)
            elif user == "scissors":
                if comp == "paper":
                    print("User: {} VS Computer: {}. User WINS!".format(user,comp))
                    u.append(1)
                    c.append(0)
                else:
                    print("User: {} VS Computer: {}. User LOSES.".format(user,comp))
                    u.append(0)
                    c.append(1)
        
            p=input("Do you want to play again? (yes/no): ")
            if p not in ["yes","y"]:
                break
    
        for i in range(len(u)):
            user_score+=u[i]
        for i in range(len(c)):
            comp_score+=c[i]
        
        print("The scores of User is {} - total: {}".format(u,user_score))
        print("The scores of Computer is {} - total: {}".format(c,comp_score))

if __name__== "__main__":
    a=rps()
    a.game()