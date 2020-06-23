"""On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor, and you can either 
start from the step with index 0, or the step with index 1."""

stairCost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

def minCost(item):
    item += [0]
    for i in range(2, len(item)): # 2 steps can be taken
        item[i] += min(item[i-1], item[i-2])
    return item[-1]

print(minCost(stairCost))