from typing import Optional,List
import json
from collections import deque

class TreeNode:
    def __init__(self,val:int = 0,left:Optional['TreeNode']=None,right:Optional['TreeNode']=None) -> Optional['TreeNode']:
        self.val = val
        self.left = left
        self.right = right


def create_tree(arr:List[int]) -> Optional[TreeNode]:
    root = TreeNode(arr[0])
    queue = deque()
    queue.append(root)
    n = len(arr)
    i = 1
    while i < n:
        node = queue.popleft()
        if i<n and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i<n and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root 

def dfs(root:Optional[TreeNode],ans:List[int]) -> None:
    if not root: return 
    dfs(root.left,ans)
    ans.append(root.val)
    dfs(root.right,ans)

def function(root:Optional[TreeNode],k:int) -> int:
    if not root: return -1

    ans = []
    dfs(root,ans)

    return ans[k-1]


if __name__ == "__main__":
    arr = json.loads(input())
    root = create_tree(arr)
    k = int(input())
    print(function(root,k))