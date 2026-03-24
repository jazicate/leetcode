# 200. Number of Islands - Medium
class Solution:
    def dfs(self, grid, m, n, i, j):
        # Check boundary and if seen
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return

        grid[i][j] = '0'

        # Visit neighbors
        self.dfs(grid, m, n, i+1, j)
        self.dfs(grid, m, n, i-1, j)
        self.dfs(grid, m, n, i, j+1)
        self.dfs(grid, m, n, i, j-1)
        

    def numIslands(self, grid: List[List[str]]) -> int: # O(mn) time, O(mn) space (recursion stack if all cells are '1')
        '''
            An island is basically "1" surrounded by "0" on left, right, top, bottom.
            All four edges of the grid are all surrounded by water.

            DFS

            initialize island count var

            loop through every cell
            if cell is "1":
                - increment island count
                - run DFS recursively
        '''

        if not grid: # If no grid, just return 0 islands
            return 0

        m = len(grid)
        n = len(grid[0])

        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_count += 1
                    self.dfs(grid, m, n, i, j)
        
        return island_count

