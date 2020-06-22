"""Given an integer array nums, find the contiguous subarray
 (containing at least one number) which has the largest sum and return its sum."""

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubaray(item):
    for i in range(len(item)):
         item[i] = max(item[i-1]+item[i], item[i])
    print(item)
    return max(item)

print(maxSubaray(nums))
