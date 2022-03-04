# https://www.acmicpc.net/problem/2210

data = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,2,1],
    [1,1,1,1,1]
]
# data = []
# for _ in range(5):
#     data.append(list(map(int, input().split())))

save = set()

# 재귀
move = [(1,0),(-1,0),(0,1),(0,-1)]
def solution(r, c, num):
    global save
    if len(num) == 6:
        save.add(num)
        return
    for i in range(4):
        nr = r + move[i][0]
        nc = c + move[i][1]
        if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
            solution(nr, nc, num + str(data[nr][nc]))

for r in range(5):
    for c in range(5):
        num = str(data[r][c])
        solution(r, c, num)

print(len(save))