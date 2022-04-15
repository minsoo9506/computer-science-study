# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기

n = int(input())
nums = list(map(int, input().split()))
math = list(map(int, input().split()))

min_val = int(1e9)
max_val = - int(1e9)
def backTracking(idx, total):
    global min_val, max_val
    if idx == n - 1:
        min_val = min(min_val, total)
        max_val = max(max_val, total)
        return

    for i in range(4):
        tmp = total
        # 연산
        if math[i] == 0:
            continue
        if i == 0:
            total += nums[idx + 1]
        elif i == 1:
            total -= nums[idx + 1]
        elif i == 2:
            total *= nums[idx + 1]
        else:
            if total >= 0:
                total //= nums[idx + 1]
            else:
                total = abs(total) // nums[idx + 1] * (-1)

        math[i] -= 1
        backTracking(idx + 1, total)
        math[i] += 1
        total = sum