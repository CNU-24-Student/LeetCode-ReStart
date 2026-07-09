from typing import List
import json

def function(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        
        # 如果中间元素大于右边界元素，说明最小值在右半部分
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            # 否则最小值在左半部分（包括mid）
            r = mid
    
    return nums[l]

if __name__ == "__main__":
    arr = json.loads(input())
    # target = int(input())
    print(function(arr))
    