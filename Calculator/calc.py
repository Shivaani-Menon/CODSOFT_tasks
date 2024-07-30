class Calculator():

    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        return n1/n2
    
    num1=float(input("Enter First Number: "))
    num2=float(input("Enter Second Number: "))

    while True:
        operation=int(input("Choose an Operation: (1) Addition  (2) Subtraction  (3) Multiplication  (4) Division :- "))
        match operation:
            case 1:
                print(add(num1,num2))
                break
            case 2:
                print(sub(num1,num2))
                break
            case 3:
                print(mul(num1,num2))
                break
            case 4:
                print(div(num1,num2))
                break
            case _:
                print("ERROR: Enter appropriate operation (1/2/3/4)")

if __name__=="__main__":
    Calculator()