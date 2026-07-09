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

def function(list1:Optional[ListNode],list2:Optional[ListNode]) -> Optional[ListNode]:
    l1,l2 = list1,list2
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            cur = cur.next
            l1 = l1.next
        else:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2

    return dummy.next


if __name__ == "__main__":
    arr1 = json.loads(input())
    head1 = createList(arr1)
    arr2 = json.loads(input())
    head2 = createList(arr2)
    printList(function(head1,head2))