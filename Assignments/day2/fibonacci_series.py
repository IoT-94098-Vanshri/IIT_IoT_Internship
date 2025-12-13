def fibonacci(n):
    a=0
    b=1
    sum=0

    for i in range(2, n):
        sum=a + b
        print(sum)
        a=sum
        b+=1
        
n = int(input("Enter how many terms: "))
fibonacci(n)