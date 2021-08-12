n = 7
t = [3,5,1,1,2,4,2]
p = [10,20,10,20,15,40,200]
dp = [0] * (n + 1)
max_val = 0

# 거꾸로 확인한다
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_val)
        max_val = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_val

print(max_val)