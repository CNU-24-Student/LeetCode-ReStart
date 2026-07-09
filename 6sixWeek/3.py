# 无重复最长子串
from typing import List
import json
from collections import defaultdict

def function(s:str) -> int:
    if not s: return 0
    n = len(s)
    ans = 0
    cnt = defaultdict(int)
    cnt[s[0]] = 1
    j = 0
    for i in range(1,n):
        while j < i and cnt[s[i]] > 0:
            cnt[s[j]] -= 1
            j += 1
        ans = max(ans,i-j+1)
        cnt[s[i]] += 1
    return ans

if __name__ == "__main__":
    s = input()
    print(function(s))