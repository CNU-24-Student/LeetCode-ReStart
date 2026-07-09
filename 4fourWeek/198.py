from typing import List
import json

def function(nums:List[int]) -> int:
    n = len(nums)
    # 相邻两个不能都偷
    # 1:倒推,最后一步就是选或者不选
    # 选最后一个的话：dp[i] = dp[i-2] + nums[i]
    # 不选最后一个的话：dp[i] = dp[i-1]
    # 2:最小子问题，确定初始值
    # dp[0] = nums[0]、dp[1] = max(nums[0],nums[1])、dp[2] = max(nums[0]+nums[2],nums[1])
    # 3:遍历
    if n == 1: return nums[0]
    if n == 2: return max(nums[0],nums[1])
    if n == 3: return max(nums[0]+nums[2],nums[1])
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    dp[2] = max(nums[0]+nums[2],nums[1])
    for i in range(3,n):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    return dp[n-1]

if __name__=="__main__":
    arr = json.loads(input())
    print(function(arr))