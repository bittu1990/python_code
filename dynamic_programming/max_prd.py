"""Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1)."""
nums = [3,4,5,2]


def max_prd(item):
    result = 0
    for i in range(len(item)-1):
        result = max(result , item[i]*item[i+1])
    return result


print(max_prd(nums))
