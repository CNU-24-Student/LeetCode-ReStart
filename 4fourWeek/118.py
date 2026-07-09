from typing import List

def function(numRows:int) -> List[List[int]]:
    ans = []
    dp = [[0]*numRows for _ in range(numRows)]
    dp[0][0] = 1
    ans.append([1])
    for i in range(1,numRows):
        for j in range(i+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        ans.append(dp[i][:i+1])

    return ans


if __name__ == "__main__":
    numRows = int(input())
    print(function(numRows))