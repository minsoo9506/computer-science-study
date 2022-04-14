# https://www.acmicpc.net/problem/1541

equation = input().split('-')

result = 0
for num in equation[0].split('+'):
    result += int(num)

for i in equation[1:]:
    for num in i.split('+'):
        result -= int(num)

print(result)