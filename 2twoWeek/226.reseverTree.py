# 左换右，右换左
from typing import Optional,List
import json
from collections import deque

class TreeNode:
    def __init__(self,val:int=0,left:Optional['TreeNode'] = None,right:Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def create_Tree(arr:List[int]) -> Optional[TreeNode]:
    root = TreeNode(arr[0])
    queue = deque()
    queue.append(root)
    cur = root
    i = 1
    n = len(arr)
    while i < n and queue:
        cur = queue.popleft() # 出队
        if i<n and arr[i]:
            node = TreeNode(arr[i])
            cur.left = node
            queue.append(node)
        i += 1
        if i<n and arr[i]:
            node = TreeNode(arr[i])
            cur.right = node
            queue.append(node)
        i += 1
    return root

def printTree(root:Optional[TreeNode]) -> None:
    if root == None:return
    arr = []
    queue = deque()
    queue.append(root)
    arr.append(root.val)
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            arr.append(node.left.val)
        if node.right:
            queue.append(node.right)
            arr.append(node.right.val)
    print(arr)

def resverse(root:Optional[TreeNode],left:Optional[TreeNode],right:Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None:return None
    root.left = right
    root.right = left
    if root.left:
        resverse(root.left,root.left.left,root.left.right)
    if root.right:
        resverse(root.right,root.right.left,root.right.right)
    return root

def function(root:Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:return None
    return resverse(root,root.left,root.right)
    
if __name__ == "__main__":
    arr = json.loads(input())
    root = create_Tree(arr)
    root = function(root)
    printTree(root)
    