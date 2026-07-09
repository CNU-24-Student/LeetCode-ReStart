from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int=0,next:Optional['ListNode'] = None) -> Optional['ListNode']:
        self.val = val
        self.next = next

def create_list(arr:List[int]) -> Optional[ListNode]:
    head = ListNode(arr[0])
    curr = head
    for i in range(1,len(arr)):
        temp = ListNode(arr[i])
        curr.next = temp
        curr = temp
    return head

def function(head:Optional[ListNode],n:int) -> Optional[ListNode]:
    if not head: return None
    dummyHead = ListNode(0)
    dummyHead.next = head
    cur = dummyHead
    left = cur.next
    while cur and left:
        if left.next == None:
            return dummyHead.next
        right = left.next
        cur.next = right
        left.next = right.next
        right.next = left
        cur = left
        left = cur.next

    return dummyHead.next

def create_list(arr:List[int]) -> None:
    head = ListNode(arr[0])
    curr = head
    for i in range(1,len(arr)):
        temp = ListNode(arr[i])
        curr.next = temp
        curr = temp
    return head

def printList(head:Optional[ListNode]) -> None:
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next
    print(ans)

if __name__ == "__main__":
    arrA = json.loads(input())
    head = create_list(arrA)
    curr = function(head,0)
    printList(curr)
    