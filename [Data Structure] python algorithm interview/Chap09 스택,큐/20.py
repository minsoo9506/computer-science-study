# 유효한 괄호
input_val = '{}[]()'

def isValid(s: str) -> bool:
    stack = []
    table = {
        '}' : '{',
        ']' : '[',
        ')' : '(', 
    }

    for val in input_val:
        if val not in table: # 열린괄호 넣기
            stack.append(val)
        elif not stack or table[val] != stack.pop():
            return False
        else:
            return len(stack) == 0