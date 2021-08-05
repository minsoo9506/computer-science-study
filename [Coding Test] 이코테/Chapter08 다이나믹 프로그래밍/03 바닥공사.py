N = 3

d = [0] * N

d[0] = 1
d[1] = 3

for i in range(2, N):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[N-1])