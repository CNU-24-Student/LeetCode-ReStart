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

def function(head:Optional[ListNode]) -> Optional[ListNode]:
    if not head:return None
    dummy = ListNode(-1)
    dummy.next = None
    cur = head
    while cur:
        next = cur.next
        cur.next = dummy.next
        dummy.next = cur
        cur = next

    return dummy.next

if __name__ == "__main__":
    arr = json.loads(input())
    head = createList(arr)
    printList(function(head))
    