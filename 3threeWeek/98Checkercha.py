from typing import Optional,List
import json
from collections import deque

class TreeNode:
    def __init__(self,val:int = 0,left:Optional['TreeNode']=None,right:Optional['TreeNode']=None) -> Optional['TreeNode']:
        self.val = val
        self.left = left
        self.right = right


def create_tree(arr:List[int]) -> Optional[TreeNode]:
    if not arr: return None
    root = TreeNode(arr[0])
    queue = deque()
    queue.append(root)
    i = 1
    while i < len(arr):
        node = queue.popleft()
        if i<len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i<len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root 

def checknode(node:Optional[TreeNode],min_val:int,max_val:int) -> bool:
    if not node:return True
    if node.val <= min_val or node.val >= max_val: return False
    return checknode(node.left,min_val,node.val) and checknode(node.right,node.val,max_val)

def function(root:Optional[TreeNode]) -> bool:
    if not root: return True
    return checknode(root,float('-inf'), float('inf'))

if __name__ == "__main__":
    arr = json.loads(input())
    root = create_tree(arr)
    print(function(root))