from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int=0,next:Optional['ListNode']=None) -> Optional['ListNode'] :
        self.val = val
        self.next = next

def create_list(arr:List[int]) -> Optional['ListNode']:
    if not arr: return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        node = ListNode(arr[i])
        cur.next = node
        cur = node
    return head

def printList(head:Optional[ListNode]) -> None:
    if not head: 
        print("[]")
        return 
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next
    print(ans)

def function(headA:Optional[ListNode],headB:Optional[ListNode]) -> Optional[ListNode]:
    if headA is None: return headB
    if headB is None: return headA
    ans = ListNode(0)
    cur = ans
    l1,l2 = headA,headB
    jw = 0
    while l1 or l2:
        x1 = l1.val if l1 else 0
        x2 = l2.val if l2 else 0
        sum = x1+x2+jw
        jw = 1 if sum >= 10 else 0
        node = ListNode(sum%10)
        cur.next = node
        cur = node
        if l1:l1 = l1.next
        if l2:l2 = l2.next
    if jw == 1:
        cur.next = ListNode(1)
    return ans.next

if __name__ == "__main__":
    arrA = json.loads(input())
    arrB = json.loads(input())
    headA = create_list(arrA)
    headB = create_list(arrB)
    print(function(headA,headB))