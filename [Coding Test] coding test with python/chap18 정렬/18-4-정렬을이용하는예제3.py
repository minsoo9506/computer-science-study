# https://www.acmicpc.net/problem/2437
# 저울

n = int(input())
data = list(map(int, input().split()))

data.sort()
answer = 1 # 1 ~ (answer - 1) 까지의 값 측정가능의미
for d in data:
    if answer < d:
        break
    answer += d

print(answer)