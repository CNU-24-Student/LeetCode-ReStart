# 搜索插入位置
from typing import List
import json

def function(nums:List[int],target:int) -> int:
    n = len(nums)
    # 从数组中找到索引值，如果目标不存在就返回需要插入的位置，如果存在就直接返回
    l ,r = 0,n-1
    if nums[0] >= target:
        return 0
    if nums[n-1] < target:
        return n
    while l < r:
        mid = (l+r)//2
        if nums[mid] == target:return mid
        elif nums[mid] > target:
            r = mid
        else:
            l = mid+1
        
    return l

if __name__ == "__main__":
    arr = json.loads(input())
    target = int(input())
    print(function(arr,target))