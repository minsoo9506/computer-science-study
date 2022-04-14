# https://www.acmicpc.net/problem/2630

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def recursive(r, c, n):
    global white, blue
    color = data[r][c]
    for nr in range(r, r + n):
        for nc in range(c, c + n):
            if color != data[nr][nc]:
                recursive(r, c, n // 2)
                recursive(r, c + n // 2, n // 2)
                recursive(r + n // 2, c, n // 2)
                recursive(r + n // 2, c + n //2, n // 2)
                return
    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return

recursive(0,0,n)
print(white, blue)