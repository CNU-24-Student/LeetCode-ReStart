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

def function(headA:Optional[ListNode],headB:Optional[ListNode]) -> bool:
    if not headA or not headB:return False
    nodes = set()
    cur = headA
    while cur:
        nodes.add(cur)
        cur = cur.next
    cur = headB
    while cur:
        if cur in nodes:
            return True
        cur = cur.next

    return False
            

if __name__ == "__main__":
    arr = json.loads(input())
    headA = createList(arr)
    headB = createList(json.loads(input()))
    print(function(headA,headB))