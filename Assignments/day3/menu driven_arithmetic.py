num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

def addition(num1,num2):
    print("Addition is:",num1+num2)
def subtraction(num1,num2):
    print("Subtraction is:",num1-num2)
def multiplication(num1,num2):
    print("Multiplication is:",num1*num2)
def division(num1,num2):
    print("Division is:",num1/num2)    

choice=int(input("Enter your choice:"))
match choice:
    case 1:
        addition(num1,num2)
    case 2:
       subtraction(num1,num2)
    case 3:
        multiplication(num1,num2)
    case 4:
        division(num1,num2)
    case default:
     print("Invalid case")    