s = '02984'

result = int(s[0])

for i in s[1:]:
    if int(i) <= 1 or result <= 1:
        result += int(i)
    else:
        result *= int(i)

print(result)