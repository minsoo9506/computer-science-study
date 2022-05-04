# https://www.acmicpc.net/prlblem/10814
# 나이순정렬

n = int(input())
data = []
for _ in range(n):
    age, name = input().split()
    data.append([int(age), name])

data.sort(key=lambda x : x[0])
print(data)