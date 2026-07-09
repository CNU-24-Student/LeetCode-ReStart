from typing import List
import json

def function(s:str,wordDict:List[str]) -> bool:
    n = len(s)
    # 倒推：dp[i] = (dp[i-len(word[0])],dp[i-len(word[1])],dp[i-len(word[2])])其中有一个是True就可以
    # 最小子问题：dp[0] = True
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1,n+1):
        for word in wordDict:
            m = len(word)
            if i-m >=0 and dp[i-m] and s[i-m:i] == word:
                dp[i] = True
                break
    return dp[n]

if __name__ == "__main__":
    s = input()
    wordDict = json.loads(input())
    print(function(s,wordDict))