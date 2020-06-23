"""Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of 
the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one."""

stockPrice = [7,1,5,3,6,4]

def maxProfit(item):
    profit = 0
    for i in range(len(item)-1):
        profit = max (profit, max(item[i:]) - item[i])
    return profit
        

print(maxProfit(stockPrice))