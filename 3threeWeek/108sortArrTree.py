# 构建 平衡二叉搜索树 其实很简单
from typing import List,Optional
import json
from collections import  deque

class TreeNode:
    def __init__(self,val:int=0,left:Optional['TreeNode']=None,right:Optional['TreeNode']=None) -> Optional['TreeNode']:
        self.val = val
        self.left = left
        self.right = right

def create_tree(arr:List[int]) -> Optional[TreeNode]:
    if not arr: return None
    root = TreeNode(arr[0])
    queue = deque()
    queue.append(root)
    n = len(arr)
    i = 1
    while i < n:
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

def print_tree(root:Optional[TreeNode]) -> None:
    if not root:
        print("[]")
        return
    ans = []
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        if node.left:queue.append(node.left)
        if node.right:queue.append(node.right)

    print(ans)

def function(arr:List[int]) -> Optional[TreeNode]:
    if not arr: return None
    n = len(arr)
    l ,r = 0,n-1
    mid = (r+l)//2
    root = TreeNode(arr[mid])
    root.left = function(arr[:mid])
    root.right = function(arr[mid+1:])
    return root
    
if __name__ == "__main__":
    arr = json.loads(input())
    # root = create_tree(arr)
    print_tree(function(arr))