# 最长递增子序列
from typing import List
import json

def function(nums:List[int]) -> int:
    n = len(nums)
    dp = [1]*(n+1)
    for i in range(1,n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j]+1,dp[i])

    return max(dp)

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))