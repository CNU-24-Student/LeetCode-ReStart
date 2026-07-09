# 最长递增子序列
from typing import List
import json

def function(s:str) -> int:
    n = len(s)
    ans = 0 
    left,right = 0,0
    for i in range(n):
        if s[i] == "(":
            left += 1
        else:
            right += 1
            if left == right:
                ans = max(ans,left*2)
            elif left < right:
                left,right = 0,0
                
    left,right = 0,0
    for i in range(n-1,-1,-1):
        if s[i] == ")":
            right += 1
        else:
            left += 1
            if left == right:
                ans = max(ans,left*2)
            elif left > right:
                left,right = 0,0

    return ans
    
if __name__ == "__main__":
    print(function(input()))