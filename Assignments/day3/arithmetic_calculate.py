num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

def calculate():
    addition(num1,num2)
    subtraction(num1,num2)
    multiplication(num1,num2)
    division(num1,num2)
    remainder(num1,num2)

def addition(num1,num2):
    print("Addition is:",num1+num2)
def subtraction(num1,num2):
    print("Subtraction is:",num1-num2)
def multiplication(num1,num2):
    print("Multiplication is:",num1*num2)
def division(num1,num2):
    print("Division is:",num1/num2)    
def remainder(num1,num2):
    print("remainder is:",num1%num2)        

calculate()    