num = int(input("Enter a positive number: "))

fib1, fib2 = 0,1
sum1 = 0
sum2 = 0
for i in range  (num):
    print(fib1, end=" ")
    fib3 = fib1 + fib2
    sum2+=fib3
    fib1 = fib2
    fib2 = fib3
    sum1+=1
   
print("\n",sum2)

#recursive approach
def fibonacci(n):   
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)     