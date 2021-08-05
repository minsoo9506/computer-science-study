#### input ####
n, m = 4, 4
d = [[0] * m for _ in range(n)]
r, c, direction = 1, 1, 0
d[r][c] = 1

arr = [[1,1,1,1],
       [1,0,0,1],
       [1,1,0,1],
       [1,1,1,1]]
#### input ####

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    next_r = r + dr[direction]
    next_c = c + dc[direction]
    # 회전한 이후 정면에 가보지 않은 육지가 존재하면 이동
    if d[next_r][next_c] == 0 and arr[next_r][next_c] == 0:
        d[next_r][next_c] = 1
        r, c = next_r, next_c
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 4방향 모두 갈 수 없는 경우
    if turn_time == 4: 
        next_r = r - dr[direction]
        next_c = c - dc[direction]
        # 뒤로 갈 수 있으면 가고
        if arr[next_r][next_c] == 0:
            r = next_r
            c = next_c
        # 뒤로도 못가면 종료
        else:
            break
        turn_time = 0

print(count)
