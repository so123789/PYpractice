num = int(input("Enter a number: "))


num_str = str(num)
digits = len(num_str)

temp = num
sum1 = 0

while temp!=0:
    rem = temp%10
    sum1 = sum1  + rem**digits
    temp //=10

if (sum1==num):
    print("Armstrong number")

else:
    print("Not a Armstrong number")