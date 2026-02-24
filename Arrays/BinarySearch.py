#binary search iterative approach\#TC: O(log N) SC: O(1)
def BinarySearch(arr, target,n):
    low = 0;
    high = n - 1;
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5  
n = len(arr)
result = BinarySearch(arr, target,n)
print(result)  # Output: 4

def BinarySearchRecursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return BinarySearchRecursive(arr, target, mid + 1, high)
    else:
        return BinarySearchRecursive(arr, target, low, mid - 1)

