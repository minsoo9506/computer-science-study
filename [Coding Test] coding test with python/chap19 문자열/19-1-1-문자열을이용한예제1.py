# https://www.acmicpc.net/problem/11720
# 숫자의 합

n = int(input())
nums = input()

result = 0
for num in nums:
    result += int(num)