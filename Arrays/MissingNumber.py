def MissingNumberBrute(nums, N):
    for i in range(1,N):
        flag = False
        for j in range(0,N-1):
            if nums[j] == i:
                flag = True
                break
        if not flag:
            return i

# print(MissingNumberBrute([1, 2, 4, 6, 3, 7, 8], 8))  # Output: 5

def MissingNumberOptimal(nums, N):
    hash = [0] * (N+1)
    for num in nums:
        hash[num] = 1
    for i in range(1, N+1):
        if hash[i] == 0:
            return i
# print(MissingNumberOptimal([1, 2, 4, 6, 3, 7, 8], 8))  # Output: 5

def MissingNumberSum(nums, N):
    total = N * (N + 1) // 2
    sum_of_nums = sum(nums)
    return total - sum_of_nums
# print(MissingNumberSum([1, 2, 4, 6, 3, 7, 8], 8))  # Output: 5

def MissingNumberXOR(nums, N):
    xor_full = 0
    xor_array = 0
    for i in range(1, N + 1):
        xor_full ^= i
    for num in nums:
        xor_array ^= num
    return xor_full ^ xor_array 
print(MissingNumberXOR([1, 2, 4, 6, 3, 7, 8], 8))  # Output: 5

