# 判断是否有环
from typing import Optional,List
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

def function(head:Optional[ListNode]) -> bool:
    cur = head
    visited = set()
    while cur:
        if cur in visited:
            return True
        visited.add(cur)
        cur = cur.next
    return False    
    
if __name__=="__main__":
    arrA = json.loads(input())
    head = create_list(arrA)
    print(function(head))