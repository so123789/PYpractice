def BubbleSort(arr):
    n= len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        
        if not swapped:
            break
    return arr;

print(BubbleSort([64, 34, 25, 12, 22, 11, 90]))

# Time Complexity: O(n^2)
# Space Complexity: O(1)
#why we use the swapped variable in case for first time swap O(n ) will come 