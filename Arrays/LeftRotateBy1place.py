def LeftRotateBy1Place(nums):
    temp = nums[0]
    n = len(nums)
    for i in range(1,n):
        nums[i-1] = nums[i]
    nums[n-1] = temp
    return nums

print(LeftRotateBy1Place([1,2,3,4,5]))  # Output: [2, 3, 4, 5, 1]