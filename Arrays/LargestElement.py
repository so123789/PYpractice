#Largest Element in an Array
def LargestElement(arr):
    if len(arr) == 0:
        return None  # Return None if the array is empty
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

print(LargestElement([3, 5, 2, 9, 1]))


#Second Largest Element in Array "Better Approach" O(2N)
# def SecondLargestElement(arr):
#     if len(arr) == 0: return
#     largeElement = arr[0]
#     for num in arr:
#         if num > largeElement :
#             largeElement = num
#     secondLargeElement = -1
#     for i in range (0,len(arr)):
#         if arr[i] > secondLargeElement and arr[i]!=largeElement:
#             secondLargeElement = arr[i]

#     return secondLargeElement

# print(SecondLargestElement([3, 5, 2, 9, 1]))


#O(n)
def SecondLargestElement(arr):
    if len(arr) == 0 or len(arr) < 2: return
    largeElement = arr[0]
    secondLargeElement = float('-inf')
    for i in range(0,len(arr)):
        if (arr[i] > largeElement):
            secondLargeElement = largeElement
            largeElement = arr[i]
        elif (arr[i] > secondLargeElement and arr[i]!=largeElement):
            secondLargeElement = arr[i]
    


    return secondLargeElement 


print(SecondLargestElement([3, 5, 2, 9, 1]))