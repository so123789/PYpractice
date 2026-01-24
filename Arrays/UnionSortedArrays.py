def UnionTwoSortedArrays(arr1, arr2):
    i, j = 0, 0
    union_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not union_arr or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not union_arr or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])
            j += 1
        else:
            if not union_arr or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
            j += 1
    while i < len(arr1):
        if not union_arr or union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not union_arr or union_arr[-1] != arr2[j]:
            union_arr.append(arr2[j])
        j += 1
    return union_arr

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5, 6]
print(UnionTwoSortedArrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]


def UnionTwoSortedArraysSet(arr1, arr2):
    union_set = set(arr1).union(set(arr2))
    return sorted(list(union_set))

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5, 6] 
print(UnionTwoSortedArraysSet(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]