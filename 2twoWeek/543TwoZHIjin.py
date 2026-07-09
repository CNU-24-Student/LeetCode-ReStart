# 二叉树的直径
# 树中任意两个节点之间的最长路径的边数,这个最长路径不一定经过根节点，可能完全在左子树或右子树内部

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
    i = 1
    n = len(arr)
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
    if not root: return 
    queue = deque()
    queue.append(root)
    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(ans)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            # 更新直径：当前节点左子树深度 + 右子树深度
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # 返回当前节点的深度
            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return self.diameter
    
if __name__=="__main__":
    arr = json.loads(input())
    root = create_tree(arr)
    print(Solution().diameterOfBinaryTree(root))
    