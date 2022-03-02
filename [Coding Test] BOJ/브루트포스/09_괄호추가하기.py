# acmicpc.net/problem/16637

n = 9
a = '3+8*7-9*2' 

a = list(a)
for i in range(0, n, 2):
    a[i] = int(a[i])
m = (n - 1) // 2 # 연산자의 갯수
result = -1
for s in range(1<<m):
    ok = True
    for i in range(m - 1):
        if s&(1<<i) > 0 and s&(1<<(i + 1)) > 0: # 연속되면 문제
            ok = False
    if not ok:
        continue
    b = a[:]
    for i in range(m):
        if (s & (1<<i)) > 0:
            k = 2 * i + 1
            if b[k] == '+':
                b[k - 1] + b[k + 1]
                b[k + 1] = 0
            elif b[k] == '-':
                k[k - 1] -= b[k + 1]
                k[k] = '+'
                b[k + 1] = 0
            elif b[k] == '*':
                b[k - 1] *= b[k + 1]
                b[k] = '+'
                b[k + 1] = 0
    temp = b[0]
    for i in range(m):
        k = 2 * i + 1
        if b[k] == '+':
            temp += b[k + 1]
        elif b[k] == '-':
            temp -= b[k + 1]
        elif b[k] == '*':
            temp *= b[k + 1]
    result = max(result, temp)

print(result)