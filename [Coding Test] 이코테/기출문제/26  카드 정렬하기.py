N  = 3
data = [10, 20, 40]
data.sort()

sum_val = 0 
before = 0
for i in range(0, len(data)):
    if i > 1:
        before = sum(data[i-2:i])
    sum_val += data[i] + before

print(sum_val)