n = 10

dp = [1] * n

n2, n3, n5 = 2, 3, 5       # 각각 2,3,5를 곱한 다음 수
idx2, idx3, idx5 = 0, 0, 0 # 현재 위치

for i in range(1, n):
    dp[i] = min(n2, n3, n5)
    if n2 == dp[i]:
        idx2 += 1
        n2 = 2 * dp[idx2]
    if n3 == dp[i]:
        idx3 += 1
        n3 = 3 * dp[idx3]
    if n5 == dp[i]:
        idx5 += 1
        n5 = 5 * dp[idx5]

print(dp[n - 1])
        