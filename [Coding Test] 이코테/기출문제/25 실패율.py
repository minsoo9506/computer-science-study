N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    answer = []
    total = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)
        
        if total == 0:
            fail = 0
        else:
            fail = count / total
            
        answer.append((i, fail))
        total -= count
    
    answer = sorted(answer, key = lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    
    return answer