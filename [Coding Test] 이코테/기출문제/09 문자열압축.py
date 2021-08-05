def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 +1):
        compressed = ''
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if s[j:j+step] == prev:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                count = 1
                prev =  s[j:j+step]
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer