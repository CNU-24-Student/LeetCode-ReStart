from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int = 0,next:Optional['ListNode'] = None):
        self.val = val
        self.next = next  

class Solution:
    def function(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        visited = set()
        curr = headA
        while curr:
            visited.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in visited:
                return curr
            curr = curr.next
            

# 列表创建链表
def create_linked_list(arr:List[int]) -> Optional[ListNode]:
    if not arr:return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1,len(arr)):
        temp = ListNode(arr[i])
        curr.next = temp
        curr = temp
    return head

# 链表打印
def print_list(head:Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

if __name__ == "__main__":
    arrA = json.loads(input())
    arrB = json.loads(input())
    headA = create_linked_list(arrA)  # 创建链表A
    headB = create_linked_list(arrB)  # 创建链表B
    ans = Solution().function(headA,headB)
    print_list(ans)