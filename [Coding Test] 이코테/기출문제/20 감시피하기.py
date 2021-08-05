n = 4
board = [['s','s','s','t'],
        ['x','x','x','x'],
        ['x','x','x','x'],
        ['t','t','t','x']]

teachers = []
spaces = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 't':
            teachers.append((i, j))
        if board[i][j] == 'x':
            spaces.append((i, j))

# 선생님이 (r, c) 위치에서 학생을 발견하는지 확인하는 함수
def watch(r, c, direction):
    def _check(r, c):
        if board[r][c] == 's':
            return True
        if board[r][c] == 'o':
            return False
    # 왼쪽
    if direction == 0:
        while c >= 0:
            _check(r, c)
            c -= 1
    # 위쪽
    if direction == 1:
        while r >= 0:
            _check(r, c)
            r -= 1
    # 오른쪽
    if direction == 2:
        while c < n:
            _check(r, c)
            c += 1
    # 아래쪽
    if direction == 3:
        while r < 0:
            _check(r, c)
            r += 1

def catch_student():
    for r, c in teachers:
        for i in range(4):
            if watch(r, c, i):
                return True
    return False

from itertools import combinations
find = False

for data in combinations(spaces, 3):
    # 장애물 설치
    for r, c in data:
        board[r][c] = 'o'
    # 학생이 한명도 안걸린 경우
    if not catch_student():
        find = True
        break
    # 장애물 다시 원위치
    for r, c in data:
        board[r][c] = 'x'

if find:
    print('Yes')
else:
    print('No')