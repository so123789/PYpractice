# brute approach
def LeftRotateByKPlace(arr, k):
    n= len(arr)
    k = k%n
    temp = []
    for i in range(0,k):
        temp.append(arr[i])
    print(temp)
    for i in range(k,n):
        arr[i - k] = arr[i]
    print(arr)
    for i in range(n - k, n):
        arr[i] = temp[i - (n - k)]
    print(arr)
    return arr

LeftRotateByKPlace([1,2,3,4,5], 2)

def LeftRotateByKPlaceOptimal(arr, k):
    n = len(arr)
    k = k % n

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse the first k elements
    reverse(0, k - 1)
    # Step 2: Reverse the remaining n-k elements
    reverse(k, n - 1)
    # Step 3: Reverse the entire array
    reverse(0, n - 1)

    return arr  