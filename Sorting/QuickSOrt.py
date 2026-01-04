def QuickSort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)

        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i=low
    j=high
    while i<j:
        while i<high and arr[i]<=pivot:
            i+=1
        while arr[j]>pivot and j>low:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j]=arr[j],arr[low]
    return j

print(QuickSort([10, 7, 8, 9, 1, 5],0,5))