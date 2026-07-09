# 排序数字中查找元素的第一个和最后一个位置
from typing import List
import json

def function(nums:List[int],target:int) -> List[int]:
    n = len(nums)
    ans = [-1,-1] # 找不到位置就返回-1,-1
    l,r = 0,n-1
    while l < r:
        mid = (l+r)//2
        if nums[mid] == target:
            left,right = mid,mid
            while left >= 1 and nums[left-1] == target:
                left -= 1
            while right < n-1 and nums[right+1] == target:
                right += 1
            ans[0],ans[1] = left,right
            return ans
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1
    
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    target = int(input())
    print(function(arr,target))