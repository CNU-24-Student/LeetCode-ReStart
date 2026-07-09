from typing import List
import json

def function(nums:List[int],target:int) -> int:
    n = len(nums)
    ans = -1
    l,r = 0,n-1
    while l <=r:
        mid = (l+r)//2
        if nums[mid] == target:return mid
        elif nums[l] <= nums[mid]: # 左半部分是有序的
            if nums[l] <= target < nums[mid]:  # target可能在左半部分
                r = mid-1
            else:
                l = mid+1
        else:# 右半部分是有序的
            if nums[mid] < target <= nums[r]:
                l = mid+1
            else:
                r = mid-1
            
    # [4,5,6,7,0,1,2]
    # [0,1,2,3,4,5,6]
    
    return ans


if __name__ == "__main__":
    arr = json.loads(input())
    target = int(input())
    print(function(arr,target))