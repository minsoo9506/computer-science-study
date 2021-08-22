# 균형 이진 트리
def isbalanced(root : TreeNode):
    def check(root):
        if not root:
            return 0

        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        
        return max(left, right) + 1

    return check(root) != -1


# 트리를 리스트로 표현하면
data = ['#',1,2,2,3,4,'#','#',4,4]

def check(root_idx):
    if root_idx >= len(data) - 1:
        return 0

    if root_idx * 2 < len(data) and data[root_idx * 2] != '#':
        left = check(root_idx * 2)
    else:
        left = 0

    if root_idx * 2 + 1 < len(data) and data[root_idx * 2 + 1] != '#':
        right = check(root_idx * 2 + 1)
    else:
        right = 0

    if left == -1 or right == -1 or abs(left - right) > 1:
        return -1

    return max(left, right) + 1

result = True
if check(1) == -1:
    result = False
else:
    result = True
print(result)