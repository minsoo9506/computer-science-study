# https://www.acmicpc.net/problem/16937

h, w = 2, 2
n = 2
r = [1,2]
c = [2,1]

result = 0
for i in range(n):
    r1, c1 = r[i], c[i]
    for j in range(i + 1, n):
        r2, c2 = r[j], c[j]
        for _ in range(2):
            for _ in range(2):
                # 스티커 위아래로 붙이는 경우
                if r1 + r2 <= h and max(c1, c2) <= w:
                    tmp = r1 * c1 + r2 * c2
                    result = max(result, tmp)
                # 스티커 좌우로 붙이는 경우
                if max(r1, r2) <= h and c1 + c2 <= w:
                    tmp = r1 * c1 + r2 * c2
                    result = max(result, tmp)
                r2, c2 = c2, r2
            r1, c1 = c1, r1

print(result)