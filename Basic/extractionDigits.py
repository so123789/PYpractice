import math 
num = int(input("Enter a number"))

def extractDigits(num):
     return int(math.log10(num) + 1);

print()

def extractandPrint(num):
    while(num>0):
        rem = num%10
        num = num//10
        print(rem)
    
# extractandPrint(num)

def reverseNum(num):
    revNum = 0;
    while(num >0):
        rem = num%10
        revNum = (revNum*10) + rem
        num = num//10
    print(revNum, end=" ")

# reverseNum(num)  

def divisors(num):
    for i in range(1,num//2 + 1): #start from 1
        if(num % i == 0):
            print(i, end="  ")

# divisors(num)

divList = []
def sqrtDivisors(num):
    # other way of writing sqrt(num) it is i*i<=Num
    for i in range(1,int(num**0.5) + 1): #start from 1 
        if(num % i == 0):
            divList.append(i)
            if((num//i)!=i):
                divList.append(num//i)
        
        
sqrtDivisors(num)
# internal sorting takes O(nlogn) n=number of factors
divList.sort()
print(divList)
