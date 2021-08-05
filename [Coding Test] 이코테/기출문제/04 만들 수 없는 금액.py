have = [3, 2, 1, 1, 9]

have.sort()

target = 1
for x in have:
    if target < x:
        break
    target += x

print(target)