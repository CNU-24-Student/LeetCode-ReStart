from typing import List
import json

def function(coins:List[int],amount:int) -> int:
    # 返回最少硬币个数
    # 如果没有任何一种硬币组合就返回-1
    # 1、倒推：dp[amount] = min(dp[amount-coins[0]],dp[amount-coins[1]])
    # 2、最小子问题：dp[0] = 0
    coins.sort() # 排序
    n = len(coins)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1,amount+1):
        for j in range(n):
            if i - coins[j] < 0:
                break
            dp[i] = min(dp[i],dp[i-coins[j]]+1)

    return -1 if dp[amount] == float('inf') else dp[amount]
    
if __name__ == "__main__":
    arr = json.loads(input())
    amount = int(input())
    print(function(arr,amount))