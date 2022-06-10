# https://leetcode.com/problems/reorder-data-in-log-files/

log_file = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

letters = []
digits = []

for l in log_file:
    if l.split()[1].isdigit():  # str.isdigit(): str이 숫가로만 이루어져 있는지 T, F
        digits.append(l)
    else:
        letters.append(l)

letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
# return 값이 있는게 아니라 바로 정렬됨

print(letters + digits)
