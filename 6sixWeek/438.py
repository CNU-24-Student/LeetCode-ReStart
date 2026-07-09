# 无重复最长子串
from typing import List
import json

def function(s:str,p:str) -> List[int]:
    m = len(s)
    n = len(p)
    if m < n: return []
    ans = []
    sortP = "".join(sorted(p)) # 先对p进行排序，然后拼接s
    temps = s[:n]
    index = 0
    if "".join(sorted(temps)) == sortP:
        ans.append(index)
    for i in range(n,m):
        index += 1
        temps = temps[1:]  
        temps += s[i]
        if "".join(sorted(temps)) == sortP:
            ans.append(index)
    return ans

if __name__ == "__main__": 
    print(function(input(),input()))