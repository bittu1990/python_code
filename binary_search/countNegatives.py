"""Given a m * n matrix grid which is sorted in non-increasing order both row-wise and 
column-wise. Return the number of negative numbers in grid."""
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

#arr = [4,3,2,-1]

def countNegatives(grid):
    return sum([binary_search(arr) for arr in grid])

def binary_search(arr):
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            
            if arr[mid] < 0:
                end = mid - 1
                print('end--' + str(end))
            else: 
                start = mid + 1
                print('start--' + str(start))
        return len(arr) - start

print(countNegatives(grid))