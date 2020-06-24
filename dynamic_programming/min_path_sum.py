"""Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time."""

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

def minSumPath(grid):
    m = len(grid)
    n = len(grid[0])
    path =[[0]*(m) for i in range(n)]

    path[0][0] = grid[0][0]

    for i in range(1,n):
        path[i][0] = grid[i][0] + path[i-1][0]
    for j in range(2,m):
        path[0][j] = grid[0][j] + path[0][j-1]
    
    print(path)
    for i in range(1,n):
            for j in range(1,m):
                path[i][j]=grid[i][j]+min(path[i-1][j],path[i][j-1])
    print(path)
    return path[n-1][m-1]

print(minSumPath(grid))


