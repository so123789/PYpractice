num = int(input("Enter a positive number: "))
# sum1 = 0
# for i in range(1,num+1):
#     sum1 +=i
# print(sum1)

def sumNatural(n):
    return (n * (n + 1))//2

print(sumNatural(num))