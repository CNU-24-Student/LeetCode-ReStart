
from typing import List
import json

def function(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    # 倒推：dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
    # 最小子问题：dp[0][0] = grid[0][0];  dp[0][0,1,2,....,n-1] = dp[0][j-1] + grid[0][j]
    # dp[0][0] = grid[0][0];  dp[0,1,2,....,m-1][0] = dp[i-1][0] + grid[i][0]
    # 循环
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1,m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1,n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]
    
if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))