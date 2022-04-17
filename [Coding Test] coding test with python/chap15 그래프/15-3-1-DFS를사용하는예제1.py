# https://www.acmicpc.net/problem/1182
# 부분수열의 합

n, s = map(int, input().split())
data = list(map(int, input().split()))

result = 0

def dfs(sum_val, idx):
    global result
    if idx >= n:
        return
    sum_val += data[idx]
    if sum_val == s:
        result += 1
    dfs(sum_val - data[idx], idx + 1) # idx 해당 수를 선택하지 않는 경우
    dfs(sum_val, idx + 1)             # idx 해당 수를 선택하는 경우

dfs(0, 0)
print(result)