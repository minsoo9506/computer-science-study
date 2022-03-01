# https://www.acmicpc.net/problem/16936

n = 6
data = [4, 8, 6, 3, 12, 9]

for i in range(n):
    num = data[i]
    cnt = 0
    while num % 3 == 0:
        num //= 3
        cnt += 1
    data[i] = (-cnt, data[i]) # sort는 오름차순이므로 음수부호를 이용

data.sort()
result = [d[1] for d in data]
print(*result, sep=' ')