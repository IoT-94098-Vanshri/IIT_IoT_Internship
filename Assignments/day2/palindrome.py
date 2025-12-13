num=int(input("Enter 5 digit number:"))
original=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10

if original==rev:
        print("Palindrome Number")
else:
        print("Not a Palindrome Number")