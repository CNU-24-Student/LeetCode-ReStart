# 链表反转
from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int=0,next:Optional['ListNode']=None) -> Optional['ListNode']:
        self.val = val
        self.next = next

def create_list(arr:List[int]) -> Optional['ListNode']:
    if not arr:return None
    head = ListNode(arr[0])
    cur = head 
    i = 1
    n = len(arr)
    while i < n:
        node = ListNode(arr[i])
        cur.next = node
        cur = node
        i += 1
    return head

def function(head: Optional['ListNode']) -> Optional['ListNode']:
    if not head:
        return None
    
    prev = None
    cur = head
    while cur:
        node = cur.next
        cur.next = prev
        prev = cur 
        cur = node
    return prev

def printList(head:Optional['ListNode']) -> None:
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next
    print(ans)
    
if __name__ == "__main__":
    arr = json.loads(input())
    # arr = list(map(int,input()))
    head = create_list(arr)
    resverse = function(head)
    printList(resverse)