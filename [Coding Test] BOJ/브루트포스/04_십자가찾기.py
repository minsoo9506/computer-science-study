# https://www.acmicpc.net/problem/16924

n, m = 6, 8
grid = [
    '....*...',
    '...**...',
    '..*****.',
    '...**...',
    '....*...',
    '........'
]

result = []
def find_cross(r, c):
    global result
    for i in range(1, min(n, m)):
        if  (r - i < 0) or (r + i >= n) or (c - i < 0) or (c + i >= m):
            break
        else:
            if grid[r - i][c] == '*' and grid[r + i][c] == '*' and grid[r][c - i] == '*' and grid[r][c + i] == '*':
                result.append([r + 1, c + 1, i])
            else:
                break

for r in range(n):
    for c in range(m):
        if grid[r][c] == '*':
            find_cross(r, c)

if len(result) == 0:
    print(-1)
else:
    print(len(result))
    for i in result:
        print(' '.join(map(str, i)))