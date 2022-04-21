# https://www.acmicpc.net/problem/2156
# 포도주 시식

n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))

dp = [0] * 10001

dp[1] = data[1]
dp[2] = data[2]
for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])

print(dp[n])