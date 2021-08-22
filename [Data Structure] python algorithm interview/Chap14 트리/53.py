# 이진 탐색 트리 노드 간 최소 거리

def minDiffInBST(root):
    prev = - int(1e9)
    result = int(1e9)

    stack = []
    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        result = min(result, node.val - prev)
        prev = node.val

        node = node.right