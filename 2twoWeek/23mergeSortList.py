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

def function(lists:List[Optional[ListNode]]) -> Optional[ListNode]:
    if len(lists) == 0 : return None
    dummyHead = ListNode(0)
    dummyHead.next = None
    cur = dummyHead
    arr = []
    for i in range(len(lists)):
        head = lists[i]
        while head:
            arr.append(head.val)
            head = head.next
    arr.sort()
    for num in arr:
        temp = ListNode(num)
        cur.next = temp
        cur = temp
        
    return dummyHead.next

def printList(head:Optional[ListNode]) -> None:
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next
    print(ans)
if __name__ == "__main__":
    arrA = json.loads(input())
    lists = []
    for i in range(len(arrA)):
        head = create_list(arrA[i])
        lists.append(head)
    curr = function(lists)
    printList(curr)