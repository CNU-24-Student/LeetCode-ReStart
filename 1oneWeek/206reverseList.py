from typing import List,Optional
import json

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def function(head:Optional[ListNode]) -> Optional[ListNode]:
    # 传入的是没有头节点的
    dummyHead = ListNode(0)
    dummyHead.next = head
    cur = dummyHead.next
    dummyHead.next =None
    while cur:
        temp = cur.next
        cur.next = dummyHead.next
        dummyHead.next = cur
        cur = temp
    return dummyHead.next

def create_list_arr(arr:List[int]) -> Optional[ListNode]:
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1,len(arr)):
        temp = ListNode(arr[i])
        curr.next = temp
        curr = temp
    return head

def printList(head:Optional[ListNode]):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

if __name__ == "__main__":
    arr = json.loads(input()) # 数组
    head = create_list_arr(arr)
    ans = function(head)
    printList(ans)