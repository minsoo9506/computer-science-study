data = '123024'

left = 0
right = 0
n = len(data)

for i in range(n // 2):
    left += int(data[i])
    right += int(data[n // 2 + i])

if left == right:
    print('Lucky')
else:
    print('Ready')