from typing import List
import json

def function(m:int,n:int) -> int:
    # 状态倒推：dp[i][j] = dp[i][j-1] + dp[i-1][j]
    # 最小子问题：dp[0][0,1,....,n-1] = 1    dp[0,1,2,3..,m-1][0] = 1
    # 循环
    dp = [[0]*n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    print(function(m,n))