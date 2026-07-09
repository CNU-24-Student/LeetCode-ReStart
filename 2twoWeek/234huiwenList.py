from typing import List,Optional
import json

class ListNode:
    def __init__(self,val:int = 0,next:Optional['ListNode'] = None) -> Optional['ListNode']:
        self.val = val
        self.next = next
    
def create_List(arr:List[int]) -> Optional[ListNode]:
    head = ListNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        temp = ListNode(arr[i])
        cur.next = temp
        cur = temp
    return head

def printList(head:Optional[ListNode]) -> None:
    cur = head
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next
    # print(",".join(str(num) for num in ans))  # 1,2,3,4
    print(ans)  # [1, 2, 3, 4] 有空格

def function(head:Optional[ListNode]) -> bool:
    # 转为数组，然后看反转后的数组是不是等于原始数组，如果是的话那就返回true
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    if arr == arr[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    arrA = json.loads(input())
    head = create_List(arrA)
    print(function(head))