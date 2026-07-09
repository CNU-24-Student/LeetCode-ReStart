# 给你一个链表，删除链表的倒数第 n 个结点
from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int=0,next:Optional['ListNode']=None) -> Optional['ListNode']:
        self.val = val
        self.next = next


def create_List(arr:List[int]) -> Optional['ListNode']:
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    n = len(arr)
    for i in range(1,n):
        node = ListNode(arr[i])
        cur.next = node
        cur = node

    return head

def printList(head:Optional['ListNode']) -> None:
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next
    print(ans)

def function(head:Optional['ListNode'],n:int) -> Optional['ListNode']:
    pre,after = head,head
    while pre and n > 0:
        pre = pre.next
        n -= 1
    
    while pre.next:
        pre = pre.next
        after = after.next
    
    if after.next:
        after.next = after.next.next
    else:
        after.next = None
    return head

    

if __name__ == "__main__":
    arr = json.loads(input())
    head = create_List(arr)
    n = int(input())
    printList(function(head,n))