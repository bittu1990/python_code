"""We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, 
and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  
Return the weight of this stone (or 0 if there are no stones left.)"""

stones = [2,2]

def lastStoneWeight(stones):
    stones.sort(reverse = True )
    while len(stones) > 1:
        stones = sorted(stones, reverse = True)
        for i in range(len(stones) - 1):

                if stones[i] == stones[i+1]:
                    stones.pop(i)
                    stones.pop(i)
                    break
                
                if stones[i] != stones[i+1]:
                    stones.append(stones[i] - stones[i+1])
                    stones.pop(i)
                    stones.pop(i)
                    break

    return 0 if len(stones) == 0 else stones[0]

print(lastStoneWeight(stones))