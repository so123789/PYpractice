def IntersectionBruteForce(arr1, arr2):
    intersection = []
    for i in arr1:
        if i in arr2 and i not in intersection:
            intersection.append(i)
    return intersection 

def IntersectionOptimal(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersection = set1.intersection(set2)
    return list(intersection)

def IntersectionTwoPointer(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i, j = 0, 0
    intersection = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not intersection or intersection[-1] != arr1[i]:
                intersection.append(arr1[i])
            i += 1
            j += 1
    return intersection

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 3, 5, 6]      
print(IntersectionBruteForce(arr1, arr2))  # Output: [2, 3]
print(IntersectionOptimal(arr1, arr2))     # Output: [2, 3]
print(IntersectionTwoPointer(arr1, arr2))  # Output: [2, 3]