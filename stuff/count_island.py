"""Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water."""

from typing import get_args


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def numIslands(grid):
    if grid == None or len(grid) == 0:
        return 0
        
    island_cnt = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                island_cnt += dfs(grid, i, j)
        
    return island_cnt
    
def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
        return 0
        
    grid[i][j] = "0"
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
    return 1


print(numIslands(grid))




        



