# 전화번호 문자 조합
digits = input()

def letterCombination(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        
        for idx in range(index, len(digits)):
            for letter in dic[digits[idx]]:
                dfs(idx+1, path+letter)

    # 예외처리
    if not digits:
        return []

    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []
    dfs(0, '')

    return result

result = letterCombination(digits)
print(result)