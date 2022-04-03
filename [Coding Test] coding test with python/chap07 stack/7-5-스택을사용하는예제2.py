# https://www.acmicpc.net/problem/10799

bar = input()
stack = []
result = 0
for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(i)
    else:
        if bar[i - 1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)