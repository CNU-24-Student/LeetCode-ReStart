from typing import Optional,List
import json
from collections import deque

class TreeNode:
    def __init__(self,val:int = 0,left:Optional['TreeNode'] = None,right:Optional['TreeNode'] = None) -> Optional['TreeNode']:
        self.val = val
        self.left = left 
        self.right = right

def build_tree(arr:List[int]) -> Optional[TreeNode]:
    if not arr: return None
    n = len(arr)
    root = TreeNode(arr[0])
    queue = deque()
    queue.append(root)
    # 按照顺序分配左右孩子就行
    i = 1
    while i < n and queue:
        node = queue.popleft()
        if i < n and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < n and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

def printTree(root:Optional[TreeNode]) -> None:
    if not root: return None
    ans = []
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(ans)
    
if __name__ == "__main__":
    arr = json.loads(input())
    root = build_tree(arr)
    printTree(root)
    