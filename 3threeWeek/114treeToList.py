from typing import List,Optional
import json
from collections import deque

class TreeNode:
    def __init__(self,val:int=0,left:Optional['TreeNode'] =None,right:Optional['TreeNode']=None) -> Optional['TreeNode']:
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self,val:int = 0,next:Optional['ListNode']=None) -> Optional['ListNode']:
        self.val = val
        self.next = next

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

def printList(head:Optional[ListNode]) -> None:
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    print(ans)

def dfs(root:Optional[TreeNode],ans:List[int]) -> None:
    if not root:return 
    ans.append(root.val)
    dfs(root.left,ans)
    dfs(root.right,ans)
    
def function(root:Optional[TreeNode]) -> Optional[ListNode]:
    # 单链表就是先序遍历拼接得到的
    if not root: return None
    ans = []
    dfs(root,ans)
    dummyHead = ListNode(0)
    cur = dummyHead
    for i in range(len(ans)):
        node = ListNode(ans[i])
        cur.next = node
        cur = cur.next
    return dummyHead.next
    
if __name__== "__main__":
    arr = json.loads(input())
    root = create_tree(arr)
    list = function(root)
    printList(list)



# def dfs(root:Optional[TreeNode],ans:List[int]) -> None:
#     if not root:return 
#     ans.append(root.val)
#     dfs(root.left,ans)
#     dfs(root.right,ans)

# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         if not root: return None
#         ans = []
#         dfs(root,ans)
#         node = root
#         node.val = ans[0]
#         for i in range(1,len(ans)):
#             node.right = TreeNode(ans[i])
#             node.left = None
#             node = node.right
#         return 