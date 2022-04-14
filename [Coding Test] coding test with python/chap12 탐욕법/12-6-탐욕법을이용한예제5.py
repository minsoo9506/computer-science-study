# https://www.acmicpc.net/problem/1489

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

csortA = [0 for _ in range(1002)]
csortB = [0 for _ in range(1002)]

for i in range(n):
    csortA[a[i]] += 1
for i in range(n):
    csortB[a[i]] += 1

answer = 0

for i in range(1, 1001):
    while csortA[i]:
        flag = False
        for j in range(i - 1, 0, -1):
            if csortB[j]:
                flag = True
                answer += 2
                csortA[i] -= 1
                csortB[j] -= 1
                break
        if flag == False:
            break

# 무승부
for i in range(1, 1001):
    while csortA[i] and csortB[i]:
        answer += 1
        csortA[i] -= 1
        csortB[i] -= 1

print(answer)