# 最长递增子序列
from typing import List
import json

def function(nums:List[int]) -> int:
    n = len(nums)
    # 前缀积 + 后缀积
    max_pre = nums[0]
    c_pre = nums[0]
    max_suf = nums[n-1]
    c_suf = nums[0]
    for i in range(1,n):
        c_pre = c_pre*nums[i]
        max_pre = max(max_pre,c_pre)

    for j in range(n-2,-1,-1):
        c_suf = c_suf*nums[j]
        max_suf = max(max_suf,c_suf)

    return max(max_pre,max_suf)
    
if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))