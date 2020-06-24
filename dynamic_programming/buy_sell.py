# O(nk) time / O(nk) space
""" def maxProfit(prices,k):
    if len(prices) == 0:
        return 0
    
    profits = [[0 for d in prices] for t in range(k+1)]

    for t in range(1, k+1):
        maxThurFar = float('-inf')
        for d in range(1, len(prices)):
            maxThurFar = max(maxThurFar, profits[t-1][d-1] - prices[d-1])
            profits[t][d] = max(profits[t][d-1], maxThurFar + prices[d])
    return profits[-1][-1] """



# O(nk) time / O(n) space

def maxProfit(prices,k):
    if len(prices) == 0:
        return 0

    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]

    for t in range(1, k+1):
        if t % 2 ==1:
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits
        
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, previousProfits[d-1] - prices[d-1])
            currentProfits = max(currentProfits[d-1], maxThusFar + prices[d])
        
    return evenProfits[-1] if k%2 == 0 else oddProfits[-1]

