from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int=0,next:Optional['ListNode']=None) -> None:
        self.val = val
        self.next = next
        
def createList(arr:List[int]) -> Optional[ListNode]:
    n = len(arr)
    head = ListNode(arr[0])
    cur = head
    for i in range(1,n):
        node = ListNode(arr[i])
        cur.next = node
        cur = node
    return head

def printList(head:Optional[ListNode]) -> None:
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    print(arr)

    return arr

def function(headA:Optional[ListNode],headB:Optional[ListNode]) -> Optional[ListNode]:
    if not headA:return headB
    if not headB:return headA
    l1,l2 = headA,headB
    jw,sum = 0,0
    dummy = ListNode(0)
    cur = dummy
    while l1 or l2:
        x1 = l1.val if l1 else 0
        x2 = l2.val if l2 else 0
        sum = x1 + x2 + jw
        jw = 1 if sum >= 10 else 0
        node = ListNode(sum%10)
        cur.next = node
        cur = node
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    if jw:
        cur.next = ListNode(jw)
    return dummy.next

if __name__ == "__main__":
    arr1 = json.loads(input())
    head1 = createList(arr1)
    arr2 = json.loads(input())
    head2 = createList(arr2)
    printList(function(head1,head2))