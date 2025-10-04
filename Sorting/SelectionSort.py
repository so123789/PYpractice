def SelectionSort(arr):
    n= len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    
    return arr

print(SelectionSort([64, 25, 12, 22, 11]))

# Time Complexity: O(n^2)
# Space Complexity: O(1)