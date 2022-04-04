# https://www.acmicpc.net/problem/2612

n, k = map(int, input().split())
nums = list(map(int, input().split()))

stack = []
for num in nums:
    while stack and k > 0 and stack[-1] < num:
        stack.pop()
        k -= 1
    stack.append(num)

print(''.join(stack[:n - k]))