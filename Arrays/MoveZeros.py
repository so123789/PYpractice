def MoveZerosAtEnd(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    print(temp)
    count = len(temp)
    for i in range(count):
        arr[i] = temp[i]
    for i in range(count, n):
        arr[i] = 0
    print(arr)

# MoveZerosAtEnd([0,1,0,3,12])

def MoveZerosOptimal(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    for i in range(j, n):
        arr[i] = 0
    print(arr)


# MoveZerosOptimal([0,1,0,3,12])


def MoveZerosOptimalSwap(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    print(arr)  
MoveZerosOptimalSwap([0,1,0,3,12,9,5,0,0,8])