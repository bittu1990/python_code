"""Given an integer array nums, find the contiguous subarray within 
an array (containing at least one number) which has the largest product."""

arr = [-2,-2,0]

""" def maxProductSubarray(arr):
    prd = 1
    result = float('-inf')
    for i in range(len(arr)):
        if prd*arr[i] <= prd:
            prd = 1
        else:
            prd = prd*arr[i]
            result = max(result, prd)
    return result """

def maxProduct(nums):
        ## RC ##
        ## APPROACH : KADANES ALGORITHM ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # 1. Edge Case : Negative * Negative = Positive
        # 2. So we need to keep track of minimum values also, as they can yield maximum values.
   
    global_max = prev_max = prev_min = nums[0]
    for num in nums[1:]:
        curr_min = min(prev_max*num, prev_min*num, num)
        curr_max = max(prev_max*num, prev_min*num, num)
        global_max= max(global_max, curr_max)
        prev_max = curr_max
        prev_min = curr_min
    return global_max

print(maxProduct(arr))