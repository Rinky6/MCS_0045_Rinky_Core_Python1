'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        counter = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j, ROW, COL)
                    counter += 1

        return counter

    def dfs(self, grid, i, j, ROW, COL):
        if grid[i][j] == "#" or grid[i][j] == "0":
            return

        grid[i][j] = "#"

        all_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in all_directions:
            neighb_row, neighb_col = direction[0] + i, direction[1] + j
            if ROW > neighb_row >= 0 and COL > neighb_col >= 0:
                self.dfs(grid, neighb_row, neighb_col, ROW, COL)
        return
'''


'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(grid, i ,j, a):
            if 0<=i<m and 0<=j<n and grid[i][j]=='1':
                grid[i][j] = a
                dfs(grid,i+1, j, a)
                dfs(grid, i, j+1, a)
                dfs(grid, i-1, j ,a)
                dfs(grid, i, j-1, a)
        counter = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(grid, i, j, counter)
                    counter+=1
        print(grid)
        return counter-2

'''
'''
def numIslands(grid: List[List[str]]) -> int:
    total = 0

    island_coords = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '1'}

    def map_island(x, y):
        if not island_coords:
            return
        if (x, y) not in island_coords:
            return

        island_coords.remove((x, y))
        map_island(x + 1, y)
        map_island(x - 1, y)
        map_island(x, y + 1)
        map_island(x, y - 1)

    while island_coords:
        p = island_coords.pop()
        island_coords.add(p)
        map_island(*p)
        total += 1

    return total
'''
matrix = [[0, 1, 1],
          [1, 1, 1],
          [1, 1, 1],
          [0, 0, 1]]

rows = len(matrix)
col = len(matrix[0])

passengers = 0

rpos = 0
cpos = 0

for i in range(len(str(matrix))):
    if cpos < col - 1:
        if matrix[rpos][cpos + 1] == 1:
            cpos += 1
            passengers += 1
        elif matrix[rpos][cpos + 1] == 0:
            cpos += 1
    if rpos < rows - 1:
        if matrix[rpos + 1][cpos] == 1:
            rpos += 1
            passengers += 1
        elif matrix[rpos + 1][cpos] == 0:
            rpos += 1

if rpos != rows - 1 or cpos != col - 1:
    passengers = 0
print(passengers)
