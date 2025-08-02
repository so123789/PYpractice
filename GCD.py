#Brute Force GCD Algorithm
#TC: O(min(n1, n2))
def GCD(n1,n2):
    gcd = 1
    res = [];
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            res.append(i)
            gcd = i
    print(res)
    return gcd
    



print(GCD(12, 15)) 
 

#Optimal GCD Algorithm
#TC: O(log(min(n1, n2)))

def GCDOptimal(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

print(GCDOptimal(12, 14))