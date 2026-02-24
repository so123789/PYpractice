#Majority Element
#Brute Force Approach#Time Complexity: O(n^2)
def MajorityElementBruteForce(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if(nums[i] == nums[j]):
                count += 1
        if(count > len(nums) // 2):
            return nums[i]

# print(MajorityElementBruteForce([2,2,4,1,1,1,2,2,4,3,4,4,5,4,4,4,4,4,4])) #Output: 2

def MajorityElementHashMap(nums):
    count_map = {}
    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    for key, value in count_map.items():
        if value > len(nums) // 2:
            return key
# print(MajorityElementHashMap([2,2,4,1,1,1,2,2,4,3,4,4,5,4,4,4,4,4,4])) #Output: 2

def MajorityElementBoyerMoore(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
# print(MajorityElementBoyerMoore([2,2,4,1,1,1,2,2,4,3,4,4,5,4,4,4,4,4,4])) #Output: 2

def MajorityElementSorting(nums):
    nums.sort()
    return nums[len(nums) // 2] 
print("Sorting:", MajorityElementSorting([2,2,4,1,1,1,2,2,4,3,4,4,5,4,4,4,4,4,4])) #Output: 2

def MajorityElementDivideAndConquer(nums):
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    left_majority = MajorityElementDivideAndConquer(nums[:mid])
    right_majority = MajorityElementDivideAndConquer(nums[mid:])

    if left_majority == right_majority:
        return left_majority

    left_count = nums.count(left_majority)
    right_count = nums.count(right_majority)

    return left_majority if left_count > right_count else right_majority
# print(MajorityElementDivideAndConquer([2,2,4,1,1,1,2,2,4,3,4,4,5,4,4,4,4,4,4])) #Output: 2

def MajorityElementMooreVoting(nums):
    count = 0
    for i in range (len(nums)):
        if count == 0:
            count = 1
            element = nums[i]
        elif element == nums[i]:
            count += 1
        else:
            count -= 1
    return element

    for i in range (len(nums)):
        if nums[i] == element:
            count += 1
    if count > len(nums) // 2:
        return element
# print(MajorityElementMooreVoting([2,2,4,1,1,1,2,2,4,3,4,4,5,4,4,4,4,4,4])) #Output: 2