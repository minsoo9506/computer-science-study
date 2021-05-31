# 이진 트리 직렬화
import collections

def serialize(root: TreeNode) -> str:
    queue = collections.deque([root])
    result = ['#']
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append('#')

    return result