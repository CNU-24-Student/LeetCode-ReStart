# 层序遍历
# 一个队列就可以
# 返回的是一个二维数组
from typing import List,Optional
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

def function(root:Optional[TreeNode]) -> List[List[int]]:
    if not root:return []
    queue = deque()
    queue.append(root)
    ans = []
    while queue:
        n = len(queue)
        cur = []
        while n:
            node = queue.popleft()
            cur.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            n -= 1
        ans.append(cur) 
    return ans

if __name__ =="__main__":
    arr = json.loads(input())
    # arr = list(map(int,input().split()))
    root = create_tree(arr)
    # print_tree(root)  # 打印树
    print(function(root))
    