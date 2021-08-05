num = [3, 4, 5]
add = 1
sub = 0
mul = 1
div = 0

# 중복순열
# from itertools import product
# print(list(product(['+','-','*','/'], repeat=(add+sub+mul+div))))

min_val = 1e9
max_val = -1e9

def dfs(i, now):
    global min_val, max_val, add, sub, mul, div
    if i == len(num):
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, now // num[i])
            div += 1

dfs(1, num[0])
print(max_val)
print(min_val)