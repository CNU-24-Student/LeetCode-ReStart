from typing import List,Optional
import json
from collections import deque

class TreeNode:
    def __init__(self,val:int=0,left:Optional['TreeNode'] =None,right:Optional['TreeNode']=None) -> Optional['TreeNode']:
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

def function(root:Optional[TreeNode]) -> List[int]:
    # 取每一层最右侧的值,层序遍历
    ans = []
    if not root: return ans
    queue = deque([root])
    while queue:
        n = len(queue)
        while n:
            node = queue.popleft()
            if n == 1:
                ans.append(node.val)
            n -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
    
if __name__== "__main__":
    arr = json.loads(input())
    root = create_tree(arr)
    printTree(root)
    print(function(root))