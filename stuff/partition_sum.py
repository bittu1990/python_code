"""Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of
 elements in both subsets is equal.

Note:

1. Each of the array element will not exceed 100.
2. The array size will not exceed 200."""

#Method 1
a = [1, 5, 11, 5,3]
def canParition(a):

    def recur(a, i , target):
        if target == 0:
            return True
        if target < 0 or i == len(a):
            return False
        if recur(a, i+1, target - a[i]):
            return True
        if recur(a, i+1, target):
            return True
        return False
    
    s = sum(a)
    if s%2 != 0:
        return False
    target = s//2

    a.sort(reverse = True)
    target -= a[0]
    return recur(a, 1, target)
    
#print(canParition(a))

#Method 2

nums = [1, 5, 11, 5]
def issubsetsum(nums, k):
    dp =set()
    for i in range(len(nums)):
        t = set(dp)
        t.add(nums[i])
        for j in dp:
            t.add(j+nums[i])

        dp = set(t)
        return k in dp

print(issubsetsum(nums,22))
