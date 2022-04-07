# https://www.acmicpc.net/problem/9375

n = int(input())

cnt_map = {}
for _ in range(n):
    key, val = input().split()
    if key in cnt_map.keys():
        cnt_map[key] += 1
    else:
        cnt_map[key] = 1

result = 1
for k in cnt_map.keys():
    result *= (cnt_map[k] + 1)
result -= 1

print(result)