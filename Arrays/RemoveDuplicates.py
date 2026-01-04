# Removed duplicates from sorted array
#Optimal Approach O(N) SC: O(1)

def RemoveDuplicates(arr):
    if len(arr) == 0:  return
    i=0
    for j in range (1, len(arr)):
        if arr[j]!= arr[i]:
            i+=1
        arr[i] = arr[j]
    return i + 1

arr = [1,2,2,3,3,4,5]
k = RemoveDuplicates(arr)
print(k)
print(arr[:k])


#using set method brute force approach

def RemoveDuplicatesSet(arr):
    if len(arr) == 0:  return

    s = set()
    j = 0
    for i in range(0, len(arr)):
        if arr[i] not in s:
            s.add(arr[i])
            arr[j] = arr[i]
            j+=1
    
    return arr[:j]

print(RemoveDuplicatesSet([2,2,4,4,5]))
