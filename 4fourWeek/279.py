from typing import List
import math

def function(n: int) -> int:
    # 倒推：dp[n] = 1 + min(dp[n - 1²], dp[n - 2²], ..., dp[n - k²])
    # 最小子问题：dp[0] = 0
    
    # 初始化 dp 数组
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # 迭代求解
    for i in range(1, n + 1):  # 从1开始更完整
        # 尝试所有可能的完全平方数 j²
        for j in range(1, int(math.sqrt(i)) + 1):
            square = j * j
            dp[i] = min(dp[i], dp[i - square] + 1)
    
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(function(n))