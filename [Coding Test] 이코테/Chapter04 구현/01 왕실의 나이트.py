#### input ####
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0] - ord('a'))) + 1
#### input ####

# 이동할 수 있는 모든 방향
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row + step[1]
    next_col = column + step[0]

    if next_row >=1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)