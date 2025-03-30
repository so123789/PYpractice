#factorial of  a number
num = int(input("Enter a positive number: "))

fact = 1
if(num==0 or num==1):
    print(1)

for i in range(1,num+1):
    fact = fact * i
print(fact)
