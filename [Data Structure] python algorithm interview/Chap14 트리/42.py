# 이진트리 최대깊이

# TreeNode class가 있다고 가정하면
import collections

def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    
    return depth

# 리스트로 이진트리 표현한 경우
tree = ['null',3,9,20,'null','null',15,7] # index 0은 사용하지 않는게 편하다
import collections

def maxDepth(root_idx = 0) -> int:
    if tree[root_idx] == 'null':
        return 0
    depth = 0
    queue = collections.deque([root_idx])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            current_node = queue.popleft()
            if current_node * 2 < len(tree) - 1 and tree[current_node * 2] != 'null':
                queue.append(current_node * 2)
            if current_node * 2 < len(tree) - 2 and tree[current_node * 2 + 1] != 'null':
                queue.append(current_node * 2 + 1)
    return depth

print(maxDepth(1))