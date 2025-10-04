# Prime number: exactly two factors 1 and the number itself
#  to check prime number or not
"""
num = int(input("Enter a positive number: "))

flag = False

if num==1:
    print("It is not a even number")
for i in range(2,num):
    if (num%i)==0:
        flag = True
        break

if(flag):
    print("Not a Prime Number")
else:
    print("It is a prime number")
"""
#prime numbers within an interval

# lower =  int(input("Enter a lower bound positive number: "))
# upper =  int(input("Enter a positive number: "))

# for num in range(lower, upper + 1):
#     if (num>1):
#         for i in range(2, num):
#             if(num%i==0):
#                 break
#         else:
#             print(num, end=" ")
# 

flag = False    

def primeOrnot(num):
    for i in range(1, (i*i < num) + 1):
        if(num%i==0):
            flag = True

            if( num//i != i):
                flag = True

# primeOrnot(7)
# print(flag)


def primeOrNot(num):
    if num <= 1:  # Numbers less than or equal to 1 are not prime
        return False

    for i in range(2, int(num**0.5) + 1):  # Check divisors up to sqrt(num)
        if num % i == 0:
            return False  # Not a prime if divisible by any number other than 1 and itself
    return True  # Prime if no divisors are found

# Example usage
num = 27
is_prime = primeOrNot(num)
print(is_prime)
