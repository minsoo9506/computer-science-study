# https://www.acmicpc.net/problem/10989
# 수 정렬하기 3

n = int(input())
count_sort = [0] * 10001

for _ in range(n):
    count_sort[int(input())] += 1
for i in range(10001):
    if count_sort[i] != 0:
        for _ in range(count_sort[i]):
            print(count_sort[i])