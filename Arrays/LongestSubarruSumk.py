def LongestSubArraySum(arr, given_sum):
    max_len = 0
    best_sub = []
    
    # i: Starting point of the subarray
    for i in range(len(arr)):
        # j: Ending point of the subarray
        for j in range(i, len(arr)):
            
            # k: Loop to manually calculate the sum from i to j
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += arr[k]
            
            # CHECK: Is this sum equal to our target?
            # This MUST be inside the 'j' loop to check every possible subarray
            if current_sum == given_sum:
                current_len = j - i + 1
                if current_len > max_len:
                    max_len = current_len
                    best_sub = arr[i : j + 1] # Slice from start to end
                    
    return max_len, best_sub

# Test
arr = [1, 2, 3, 7, 5]
k = 12
length, sub = LongestSubArraySum(arr, k)
print(f"Max Length: {length}")
print(f"Subarray: {sub}")