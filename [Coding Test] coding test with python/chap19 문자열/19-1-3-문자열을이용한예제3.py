# https://www.acmicpc.net/problem/9935
# 문자열 폭발

x = input()
bomb = input()

while bomb in x:
    if bomb == x:
        x = 'FRULA'
        break
    x = ''.join(x.split(bomb))

print(x)