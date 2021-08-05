# input
a = [1,2,3,4,5]
b = [3,4,5,6,7]
#

a.sort()
b.sort(reverse=True)

for i in range(len(a)):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(a)