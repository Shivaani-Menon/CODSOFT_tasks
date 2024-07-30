import random
import string

class passwd():
    cap=string.ascii_uppercase
    small=string.ascii_lowercase
    digits=string.digits
    symb=string.punctuation

    combo=cap+digits+small+symb

    def gen(self):
        while True:
            try:
                pass_len=int(input("Enter the desired length of password: "))
                if pass_len<=0:
                    print("ERROR: Enter a positive length value.")
                else:
                    res=""
                    for _ in range(0, pass_len):
                        res+=random.choice(self.combo)
                    print("The password is:",res)
                    p=input("Do you want another password? (yes/no): ").lower()
                    if p not in ["yes","y"]:
                        exit()
        
            except ValueError:
                print("ERROR: Enter appropriate numerical value for length.")

if __name__=="__main__":
    a=passwd()
    a.gen()