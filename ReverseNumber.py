#ReverseNumber

def ReverseNumber(n):
    temp = 0
    while n > 0:
        rem = n%10;
        temp = temp*10 +rem
        n//=10
    return temp

print(ReverseNumber(456))
    