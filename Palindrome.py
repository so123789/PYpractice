#Palindrome

def Palindrome(N):
    temp =N;
    rev = 0
    while N>0:
        rem=N%10
        rev= rev*10 + rem
        N//=10
    if temp == rev:
        return True

    else:
        return False

print(Palindrome(121))  