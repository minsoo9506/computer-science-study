# 이진트리 최대깊이
tree = [3,9,20,null,null,15,7]

import collections

def maxDepth(root: TreeNode):
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