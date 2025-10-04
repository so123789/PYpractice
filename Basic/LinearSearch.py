def LinearSearch(list1, target):
    for i in range(0, len(list1)):
        if list1[i] == target:
            return i
        return -1

    

list1 = [1,4,5,6,7]
print(LinearSearch(list1,2))