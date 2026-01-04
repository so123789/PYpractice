def RemoveElement(arr, val):
    i = 0
    temp = []
    n =len(arr)
    for j in range(0,n):
        if arr[j] != val:
            temp.append(arr[j])
            # arr[i] = arr[j]
            i += 1
        else:
            temp.append('_')
            i+=1
    return i, temp

print(RemoveElement([3,2,2,3], 3))