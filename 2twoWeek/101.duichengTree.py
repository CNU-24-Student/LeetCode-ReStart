# 看左右子树是否相等
from typing import Optional,List
import json
from collections import deque

class TreeNode:
    def __init__(self,val:int = 0,left:Optional['TreeNode'] = None,right:Optional['TreeNode'] = None) -> Optional['TreeNode']:
        self.val = val
        self.left = left
        self.right = right


def create_tree(arr:List[int]) -> Optional[TreeNode]:
    root = TreeNode(arr[0])
    queue = deque()
    queue.append(root)
    i = 1
    n = len(arr)
    while i < n and queue:
        node = queue.popleft()
        if i < n and arr[i]:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < n and arr[i]:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

def sameLR(left:Optional[TreeNode],right:Optional[TreeNode]) -> bool:
    if (not left and right) or (not right and left): return False
    if not left and not right: return True
    if left.val != right.val : return False
    return sameLR(left.left,right.right) and sameLR(left.right,right.left)

def function(root:Optional[TreeNode]) -> bool:
    if not root: return True
    return sameLR(root.left,root.right)


if __name__=="__main__":
    arr = json.loads(input())
    root = create_tree(arr)
    print(function(root))