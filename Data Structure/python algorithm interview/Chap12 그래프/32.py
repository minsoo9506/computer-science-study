# 섬의 갯수
row, col = map(int, input().split())
grid = [0] * row

for r in range(row):
    grid[r] = list(input())

def numIslands(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or\
            j < 0 or j >= len(grid[0]) or\
                grid[i][j] != '1':
                return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
                
    return count

print(grid)
count = numIslands(grid)
print(count)