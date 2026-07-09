# 最大深度就是cur = cur.left,height+1
from typing import Optional,List
import json
from collections import deque 

class TreeNode:
    def __init__(self,val:int = 0,left:Optional['TreeNode'] = None,right:Optional['TreeNode'] = None) -> Optional['TreeNode']:
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr:List[int]) -> Optional[TreeNode]:
    n = len(arr)
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while i < n:
        cur = queue.popleft()
        if i<n and arr[i] is not None:
            cur.left = TreeNode(arr[i])
            queue.append(cur.left)
        i += 1
        if i<n and arr[i] is not None:
            cur.right = TreeNode(arr[i])
            queue.append(cur.right)
        i += 1
    return root

def height_tree(root:Optional[TreeNode],height:int) -> int:
    if root == None: return height
    
    left = height_tree(root.left,height+1)
    right = height_tree(root.right,height+1)
    return max(left,right)

def function(root:Optional[TreeNode]) -> int:
    if not root: return 0
    left_height = height_tree(root.left,1)
    right_height = height_tree(root.right,1)
    return max(left_height,right_height)


if __name__ == "__main__":
    arr = json.loads(input())
    root = build_tree(arr)
    print(function(root))