from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak)
    # 원형을 일자 형태로 변환
    for i in range(weak_len):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    
    for start in range(weak_len):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + weak_len):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer