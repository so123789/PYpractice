def InsertionSort(arr):
    n=len(arr)
    for i in range(0,n):
        j = i
        while j>0 and  arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1    
    return arr

print(InsertionSort([12, 11, 13, 5, 6])) 