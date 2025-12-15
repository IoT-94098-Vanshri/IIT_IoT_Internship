num = int(input("Enter number for fact: "))
base = int(input("Enter base for power: "))
exponent = int(input("Enter exponent: "))

#fact function
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

#power function
def power(base, exponent):
    if exponent==0:
        return 1
    return base*power(base,exponent-1)

print("Factorial of number:", num, "=", fact(num))
print("Power:", base, "^", exponent, "=", power(base, exponent))