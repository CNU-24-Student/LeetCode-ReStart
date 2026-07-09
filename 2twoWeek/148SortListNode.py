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

def function(head:Optional[ListNode]) -> Optional[ListNode]:
    if not head: return head
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    arr.sort()
    return create_list(arr)

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
    curr = function(head)
    printList(curr)