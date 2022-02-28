# https://www.acmicpc.net/problem/16922

# 경우의 수: N ^ 4 가지 -> 어차피 마지막은 fix되니까 N ^ 3가지

n = int(input())

check = [False] * (50 * 20 + 1)
for i in range(n + 1):
    for j in range(n - i + 1):
        for k in range(n - i - j + 1):
            l = n - i - j - k
            sum = i + 5 * j + 10 * k + 50 * l
            check[sum] = True

result = 0
for i in range(1, 50 * 20 + 1):
    if check[i]:
        result += 1

print(result)