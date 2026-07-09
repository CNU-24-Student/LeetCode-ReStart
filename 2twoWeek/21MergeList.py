# 合并两个有序链表,得到升序链表
from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int = 0,next:Optional['ListNode'] = None) -> Optional['ListNode']:
        self.val = val
        self.next = next

def create_list(arr:List[int]) -> Optional[ListNode]:
    head = ListNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        temp = ListNode(arr[i])
        cur.next = temp
        cur = temp
    return head

def function(listA:Optional[ListNode],listB:Optional[ListNode]) -> Optional[ListNode]:
    h1 = listA
    h2 = listB
    ans = ListNode(0)
    cur = ans
    while h1 and h2:
        if h1.val <= h2.val:
            cur.next = h1
            cur = h1
            h1 = h1.next
        else:
            cur.next = h2
            cur = h2
            h2 = h2.next
    if h1:cur.next = h1
    if h2:cur.next = h2

    return ans.next

def printList(head:Optional[ListNode])->None:
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next
    print(ans)
    
if __name__ == "__main__":
    arrA = json.loads(input())
    arrB = json.loads(input())
    headA = create_list(arrA)
    headB = create_list(arrB)
    printList(function(headA,headB))