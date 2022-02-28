# https://www.acmicpc.net/problem/16968

x = 'dcdd'

if x[0] == 'c':
    result = 26
else:
    result = 10

prev = x[0]

for i in x[1:]:
    if i == 'c' and prev == 'c':
        result *= 25
        prev = 'c'
    elif i == 'c' and prev != 'c':
        result *= 26
        prev = 'c'
    elif i == 'd' and prev == 'd':
        result *= 9
        prev = 'd'
    else:
        result *= 10
        prev = 'd'
        
print(result)