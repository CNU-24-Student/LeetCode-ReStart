from typing import List
import json

def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    word_set = set(wordDict)  # 转为集合，O(1)查找
    
    # dp[i] 表示 s[0:i] 能否被拼接
    dp = [False] * (n + 1)
    dp[0] = True  # 空字符串
    
    for i in range(1, n + 1):
        for j in range(i):
            # s[0:j] 可拼接，且 s[j:i] 在字典中
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # 找到一种即可
    
    return dp[n]

if __name__ == "__main__":
    s = input().strip()
    wordDict = input().strip().split(',')
    # 去除可能的空格
    wordDict = [w.strip() for w in wordDict]
    print(wordBreak(s, wordDict))