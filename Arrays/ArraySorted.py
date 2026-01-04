#To check if an array is sorted or not O(n)

def ArraySortedOrNot(arr):
    if len(arr) == 0: return

    for i in range(0, len(arr)):
        if (arr[i] <= arr[i+1]):
            return True
        return False

print(ArraySortedOrNot([2,1,5,4,6]))
print(ArraySortedOrNot([1,1,2,2,4,5]))