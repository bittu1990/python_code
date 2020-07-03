"""A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the
conveyor belt being shipped within D days.

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 
and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 
is not allowed. """

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

def breakHalf(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

def shipWithinDays(weights, days):
    tot_weight = []
    i = 0
    while i < days:
        if i == 0:
            tot_weight.append(breakHalf(weights))
        if i != 0:
            for j in tot_weight:
                tot_weight.append(breakHalf(j))
                #tot_weight.pop(j)
        
        i += 1

    return tot_weight

print(shipWithinDays(weights,days))
    


