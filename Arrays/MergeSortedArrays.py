def MergeSortedArraysBrute(arr1, m, arr2, n):
    i = 0
    j = 0
    merged = []
    while i < m and j < n:  
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < m:
        merged.append(arr1[i])
        i += 1