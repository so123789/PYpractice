#print N time the name
# def printName(N, name, i):
#     if(i>=N):
#         return
#     print(name)
#     printName(N, name, i+1)

# printName(5,"Soup",0)

#print from 1 to N

# def Linear(N, i):
#     if(i>=N):
#         return
#     print(i, end=" ")
#     Linear(N, i+1)

# Linear(5,1)

#Backtracking
# def LinearBT(N, i):
#     if(i < 1):
#         return
#     LinearBT(N, i-1)
#     print(i, end = " ")

# LinearBT(5, 5)


#print from N to 1

# def Linear(N):
#     if(N <=0 ):
#         return
#     print(N, end=" ")

#     Linear(N-1)

# Linear(5)

# def LinearBT(N):
#     if(N<=0):
#         return
#     print(N, end = " ")
#     LinearBT(N-1)


# LinearBT(5)


#parameterised summation of N
sum=0
def summation(N, i):
    if(i<0):
        print(sum)
        return
    summation(sum+i, i-1)

summation(5, 1)
    