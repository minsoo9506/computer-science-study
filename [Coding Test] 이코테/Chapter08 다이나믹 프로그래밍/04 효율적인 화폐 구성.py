n = 15
money = [2,3,7]

d = [1000] * (n + 1) # index를 1부터 시작하도록
d[0] = 0

for i in money:
    for j in range(i, n+1):
        if d[j - i] != 1000:
            d[j] = min(d[j], d[j - i] + 1)

print(d[n])