# Iterative approach
# def BinarySearch(list1, low, high, target):
#     while (low<=high):
#         middle = low + (high - low)//2

#         if list1[middle] == target:
#             return middle

#         elif list1[middle] < target:
#             low = middle + 1
        
#         else:
#             high = middle - 1
#     return -1

# list1 = [1,3,5,6,7]
# print(BinarySearch(list1,0,len(list1)-1,7))

# Recursive Binary serach
def BinarySearch(list1, low, high, target):
    while (low<=high):
        middle = low + (high - low)//2

        if list1[middle] == target:
            return middle

        elif list1[middle] < target:
            return BinarySearch(list1, middle + 1, high, target)
        
        else:
            return BinarySearch(list1 , low , middle -1 , target)
    return -1

list1 = [1,3,5,6,7]
print(BinarySearch(list1,0,len(list1)-1,10))
