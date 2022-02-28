# https://www.acmicpc.net/problem/16917

a, b, c, x, y = map(int, input().split())
# a, b, c, x, y = 1500, 2000, 1600, 3, 2

def solution(a, b, c, x, y):
    _min = min(x, y)
    result = int(1e9)
    for i in range(_min + 1):
        result = min(2 * i * c + max(0, x - i) * a + max(0, y - i) * b, result)
    return result

print(solution(a, b, c, x, y))