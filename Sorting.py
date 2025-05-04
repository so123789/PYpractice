# Bubble sort O(n^2)
# arr = [3,4,1,3,7,2,5]
# n = len(arr)
# for i in range(0, n-1):
#     for j in range(0, n-i-1):
#         if (arr[j] > arr[j+1]):
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

# To optimise the sorting add bollean variable  for already sorted arrays
# arr = [3,4,1,3,7,2,5]
# n = len(arr)
# isSwap = False
# for i in range(0, n-1):
#     for j in range(0, n-i-1):
#         if (arr[j] > arr[j+1]):
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             isSwap = True

    
# print(arr)

# Selection Sort

# def selectionSort (arr , n):
#     for i in range(0,n-1):
#         smallIndex = i

#         for j in range(i+1, n):
#             if(arr[j] <  arr[smallIndex]):
#                 smallIndex = j

#         arr[i], arr[smallIndex] = arr[smallIndex], arr[i]

#     return arr

# arr = [3,4,1,3,7,2,5]
# n = len(arr)

# z = selectionSort(arr, n)
# print(z)


#Insertion sort

def InsertionSort(arr, n):
    for i in range(0, n-1):
        currentIndex = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > currentIndex:
            arr[j+1] = arr[j]
            j = j -1

        arr[j+1] = currentIndex

    return arr
    
arr = [3,4,1,3,7,2,5]
n = len(arr)

print(InsertionSort(arr, n))