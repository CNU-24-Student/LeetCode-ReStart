from typing import List,Optional
import json
from collections import deque

class TreeNode:
    def __init__(self,val:int=0,left:Optional['TreeNode']=None,right:Optional['TreeNode']=None) -> Optional['TreeNode']:
        self.val = val
        self.left = left
        self.right = right

def create_tree(arr:List[int]) -> Optional[TreeNode]:
    root = TreeNode(arr[0])
    i = 1
    n = len(arr)
    queue = deque([root])
    while i<n:
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
    if not root: return
    queue = deque([root])
    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node.val)    
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(ans)


def dfs(root:Optional[TreeNode],p:Optional[TreeNode],q:Optional[TreeNode]) -> Optional[TreeNode]:
    if not q or not p or not root: return None
    if q == root:return q
    if p == root:return p
    left = dfs(root.left,p,q)
    right = dfs(root.right,p,q)
    if left and right:
        return root
    return left if left else right # 因为已经说了一定在给定的二叉树中
                
def function(root:Optional[TreeNode],p:Optional[TreeNode],q:Optional[TreeNode]) -> Optional[TreeNode]:
    if not q or not q or not root: return None
    return dfs(root,p,q)
        
if __name__ == "__main__":
    arr = json.loads(input())
    root = create_tree(arr)
    # printTree(root)

        