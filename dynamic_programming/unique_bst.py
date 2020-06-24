"""Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?"""

n =3
from functools import lru_cache
@lru_cache(None) 
def numTrees(n):
    cnt = 0
    #return 1 if n<2 else sum(numTrees(i)*numTrees(n-1-i) for i in range(0,n))

    if n<2:
        return 1
    else:
        for i in range(n):
            cnt += numTrees(i) * numTrees(n-1-i)
    return cnt

print(numTrees(n))