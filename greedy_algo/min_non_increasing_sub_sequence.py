"""Given the array nums, obtain a subsequence of the array whose sum of 
elements is strictly greater than the sum of the non included elements in such subsequence.
If there are multiple solutions, return the subsequence with minimum size and if there
still exist multiple solutions, return the subsequence with the maximum total sum of 
all its elements. A subsequence of an array can be obtained by erasing some (possibly zero)
elements from the array. 

Input: nums = [4,3,10,9,8]
Output: [10,9] 
Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their 
elements is strictly greater than the sum of elements not included, 
however, the subsequence [10,9] has the maximum total sum of its elements. 
"""
nums = [4,3,10,8,9]
#nums = [4,4,7,6,7]
def minSubsequence(nums):
    nums.sort()
    total = sum(nums)
    i = 0
    currSum = 0

    while i < len(nums):
        currSum += nums[i]
        if currSum < total - currSum:
            i += 1
        else:
            break
    print(i)
    res = nums[i:]
    return res[::-1]



print(minSubsequence(nums))




