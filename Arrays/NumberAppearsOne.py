def NumbersAppearsOnce(arr):
    n = len(arr)
    
    for i in range(0,n):
        count = 0
        for j in range(0, n):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            print(arr[i])
