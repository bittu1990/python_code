"""A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?"""

m = 7
n = 3
 ##Normal Method
def uniquePaths(m: int, n: int) -> int:
        ways = [] 
        for row in range(m) :
            ways.append([]) #new row
            
            for col in range(n) :
                ways[row].append(0)#new column
                if row == col == 0 :
                    ways[row][col] = 1
                if row > 0 : #add paths from left
                    ways[row][col] += ways[row - 1][col] 
                if col > 0 : #add paths from above
                     ways[row][col] += ways[row][col - 1]
                        
        return ways[m-1][n-1] #return bottom right

print(uniquePaths(m,n))


"""Dynamic Programming"""

def uniqueWays(m,n):
    path = [[1 for i in range(m)]for j in range(n)]

    for i in range(1,n):
        for j in range(1,m):
            path[i][j] = path[i-1][j] + path[i][j-1]
    print(path[-1][-1])

uniqueWays(m,n)