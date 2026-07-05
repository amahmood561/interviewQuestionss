class Islands:
    def __init__(self, grid):
        self.grid = grid
        self.islands = 0

    def dfs(self, r, c):
        if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]) or self.grid[r][c] == '0':
            return
        self.grid[r][c] = '0'
        self.dfs(r - 1, c)
        self.dfs(r + 1, c)
        self.dfs(r, c - 1)
        self.dfs(r, c + 1)

    def numIslands(self):
        if not self.grid:
            return 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    self.islands += 1

        return self.islands

# Create an instance of the Islands class
islands = Islands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
])
print(islands.numIslands()) # Expected output: 1

islands = Islands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])
print(islands.numIslands()) # Expected output: 3

'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''

class Islands:
    def __init__(self, grid):
        self.grid = grid
        self.islands = 0

    def dfs(self, r, c):
        if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]) or self.grid[r][c] == '0':
            return
        self.grid[r][c] = '0'
        self.dfs(r - 1, c)
        self.dfs(r + 1, c)
        self.dfs(r, c - 1)
        self.dfs(r, c + 1)

    def numIslands(self):
        if not self.grid:
            return 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    self.islands += 1

        return self.islands

# Create an instance of the Islands class
islands = Islands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
])
print(islands.numIslands()) # Expected output: 1

islands = Islands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])
print(islands.numIslands()) # Expected output: 3

'''
In this example, I've defined a class called Islands which takes a 2D binary grid as an input in the constructor. The class has two methods:

dfs(r, c) is the same as the previously defined function, but now it's a method of the Islands class, so it has access to the self.grid attribute, which stores the input grid.
numIslands() is also the same as before, but now it's a method of the Islands class, so it has access to the self.islands attribute which stores the total number of islands found in the grid.
The class instance is then created by providing the grid to the constructor, which is passed to the self.grid attribute. Finally, numIslands method is called on the class instance to get the total 
number of islands found in the grid.

Now the grid is an attribute of class and the state of the class is not modified after each call. So it can be reused multiple time with the same grid.
'''

class Islands:
    def __init__(self, grid):
        self.grid = grid
        self.islands = 0

    def bfs(self, r, c):
        queue = [(r, c)]
        while queue:
            r, c = queue.pop(0)
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == '1':
                self.grid[r][c] = '0'
                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r, c + 1))

    def numIslands(self):
        if not self.grid:
            return 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '1':
                    self.bfs(i, j)
                    self.islands += 1

        return self.islands

'''
In this example, I've replaced the DFS method for BFS, which is implemented in the bfs(self, r, c) method. This method uses a queue data structure to keep track of the cells that need to be visited.
 It starts with the initial cell (r,c), and while there are still cells in the queue, 
it pops the first one and checks if it is a land ('1'). If it is, it marks the cell as visited ('0'), and appends its neighbors to the queue.

The rest of the class remains the same, but now it's using bfs instead of dfs, making the algorithm more efficient when dealing with sparse grids and also reducing memory complexity as well.

It's also worth mentioning that both DFS and BFS have a time complexity of O(mn) where m is number of rows and n is number of cols, but in practice BFS is often slightly faster when grid is sparse.
'''