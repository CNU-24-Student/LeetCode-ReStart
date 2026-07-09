# 两数相加，两个链表的值相加
from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int = 0,next:Optional['ListNode'] = None) -> Optional['ListNode']:
        self.val = val
        self.next = next

def create_List(arr:List[int]) -> Optional[ListNode]:
    if not arr:return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        temp = ListNode(arr[i])
        cur.next = temp
        cur = temp
    return head


def function(headA:Optional[ListNode],headB:Optional[ListNode]) -> Optional[ListNode]:
    h1,h2 = headA,headB
    jw = 0
    ans = ListNode(0)
    curr = ans
    while h1 or h2:
        x1 = h1.val if h1 else 0
        x2 = h2.val if h2 else 0
        sum = x1+x2+jw
        jw = 1 if sum >= 10 else 0

        node = ListNode(sum%10)
        curr.next = node
        curr = node
        if h1:h1 = h1.next
        if h2:h2 = h2.next
    if jw == 1:
        curr.next = ListNode(jw)
    return ans.next

def printList(head:Optional[ListNode]) -> None:
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next

    print(ans)
    
if __name__ == "__main__":
    arrA = json.loads(input())
    arrB = json.loads(input())
    headA = create_List(arrA)
    headB = create_List(arrB)
    printList(function(headA,headB))