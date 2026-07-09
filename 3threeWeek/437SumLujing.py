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
    while i<n and queue:
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

def dfs(root:Optional[TreeNode],targetSum:int,curSum:int) -> int:
    if not root:return 0
    count = 0
    curSum += root.val
    if curSum == targetSum:count += 1
    count += dfs(root.left,targetSum,curSum)
    count += dfs(root.right,targetSum,curSum)
    return count 
                
def function(root:Optional[TreeNode],targetSum:int) -> int:
    # 当前节点为root，计算到每个节点的位置的sum之和
    if not root:return 0
    return dfs(root,targetSum,0) + function(root.left,targetSum) + function(root.right,targetSum)
        
if __name__ == "__main__":
    arr = json.loads(input())
    root = create_tree(arr)
    # printTree(root)
    targetSum = int(input())
    print(function(root,targetSum))
        