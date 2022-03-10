# https://www.acmicpc.net/problem/17085

n, m = 5, 6
data = [
    ['#','#','#','#','#','#'],
    ['#','.','.','.','#','.'],
    ['#','#','#','#','#','#'],
    ['#','#','.','.','#','.'],
    ['#','#','#','#','#','#']
]

# 중심과 크기로 십자가 표현
ans = 0
for r1 in range(n):
    for c1 in range(m):
        s1 = 0
        while True:
            if r1 - s1 < 0 or r1 + s1 >= n: break
            if c1 - s1 < 0 or c1 + s1 >= m: break
            if data[r1 - s1][c1] != '#' or data[r1 + s1][c1] != '#': break
            if data[r1][c1 - s1] != '#' or data[r1][c1 + s1] != '#': break
            data[r1 - s1][c1] = '*'
            data[r1 + s1][c1] = '*'
            data[r1][c1 - s1] = '*'
            data[r1][c1 + s1] = '*'
            for r2 in range(n):
                for c2 in range(m):
                    s2 = 0
                    while True:
                        if r2 - s2 < 0 or r2 + s2 >= n: break
                        if c2- s2 < 0 or c2 + s2 >= m: break
                        if data[r2 - s2][c2] != '#' or data[r2 + s2][c2] != '#': break
                        if data[r2][c2 - s2] != '#' or data[r2][c2 + s2] != '#': break
                        area = (4 * s1 + 1) + (4 * s2 + 1)
                        ans = max(ans, area)
                        s2 += 1
            s1 += 1
        s1 = 0
        while True:
            if r1 - s1 < 0 or r1 + s1 >= n: break
            if c1 - s1 < 0 or c1 + s1 >= m: break
            if data[r1 - s1][c1] != '*' or data[r1 + s1][c1] != '*': break
            if data[r1][c1 - s1] != '*' or data[r1][c1 + s1] != '*': break
            data[r1 - s1][c1] = '#'
            data[r1 + s1][c1] = '#'
            data[r1][c1 - s1] = '#'
            data[r1][c1 + s1] = '#'
            s1 += 1

print(ans)