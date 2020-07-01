"""There are 2N people a company is planning to interview.
The cost of flying the i-th person to city A is costs[i][0], and the cost of 
flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly
 N people arrive in each city."""

costs = [[10,20],[30,200],[400,50],[30,20]]

def twoCitySchedCost(costs):
    # D.F = move to City B NOT to City A! step 1 and step 2 combined!!
        costs.sort(key = lambda x: x[1]-x[0])
        
        # variable to store the total cost
        res=0
        
        # sending first half to city B and remaining to city A
        for i in range(len(costs)):
            if i<len(costs)//2:
                res+=costs[i][1]
            else:
                res+=costs[i][0]
        
        return res
print(twoCitySchedCost(costs))
