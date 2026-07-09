from typing import List
import json

def function(n:int) -> int:
    dp = [0]*n
    # 1、反推，最后一个台阶，是从倒数第二个台阶+倒数第三个台阶
    # dp[n] = dp[n-1] + dp[n-2]
    # 2、确定边界，最小子问题解
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

if __name__ == "__main__":
    # arr = json.loads(input())
    n = int(input())
    print(function(n))