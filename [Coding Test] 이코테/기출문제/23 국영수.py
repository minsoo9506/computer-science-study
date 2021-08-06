data = [('Kim', 90, 60, 100),
        ('Song', 80, 60, 50),
        ('Park', 80, 70, 100)]

data.sort(key=lambda x : (-int(x[1]), x[2], -int(x[3]), x[0]))

print(data)