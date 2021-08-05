n, m = 4, 5
input_data = [[0,0,1,1,0],
              [0,0,0,1,1],
              [1,1,1,1,1],
              [0,0,0,0,0]]

def dfs(row, col):
    # 전체 범위를 벗어난 경우
    if row < 0 or row >= n or col < 0 or col >= m:
        return False
    # 현재 위치를 방문하지 않았거나 원래 0인 경우
    if input_data[row][col] == 0:
        # 방문처리
        input_data[row][col] = 1
        # 상하좌우 dfs
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)
        return True
    return False

result = 0
for r in range(n):
    for c in range(m):
        if dfs(r, c):
            result += 1

print(result)
