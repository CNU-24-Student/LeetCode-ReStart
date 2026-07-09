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

def transver(root:Optional[TreeNode],ans:List[int]) -> None:
    if root == None: return 
    transver(root.left,ans)
    ans.append(root.val)
    transver(root.right,ans)
    

# def function(root:Optional[TreeNode]) -> List[int]:
#     if not root: return []
#     ans = []
#     # 左根右
#     transver(root,ans)
#     return ans

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root: return []
    # 中序遍历就是一直先遍历左子树
    cur = root
    ans = []
    stack = []
    while cur or stack:
        while cur:
            stack.append(cur) # 根入栈
            cur = cur.left  # 左子树入栈
        cur = stack.pop()
        ans.append(cur.val)
        cur = cur.right # 右子树        

    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    root = build_tree(arr)
    ans = function(root)
    print(ans)