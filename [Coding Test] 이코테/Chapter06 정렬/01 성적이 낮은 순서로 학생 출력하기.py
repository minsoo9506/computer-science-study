# input
arr = [('홍길동', 95), ('이순신', 77),('김두한', 88)]

sorted_arr = sorted(arr, key = lambda student : student[1])

for student in sorted_arr:
    print(student[0], end = ' ')