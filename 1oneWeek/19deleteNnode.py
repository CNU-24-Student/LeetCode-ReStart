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
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    while n:
        fast = fast.next
        n-=1
    while fast.next:
        fast = fast.next
        slow = slow.next
    temp = slow.next
    slow.next = None if temp.next == None else temp.next
    return dummy.next

def printList(head:Optional[ListNode]) -> None:
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next
    print(ans)

if __name__ == "__main__":
    arrA = json.loads(input())
    n = int(input())
    head = create_list(arrA)
    curr = function(head,n)
    printList(curr)