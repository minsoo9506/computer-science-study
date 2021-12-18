# 왼쪽에서 오른쪽, 위에서 아래쪽으로 정렬된 data
data = [[1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]]

target = 5

# 이진검색이 복잡해서 이렇게 ㅎㅎ
def solution(data, target):
    return any(target in row for row in data)