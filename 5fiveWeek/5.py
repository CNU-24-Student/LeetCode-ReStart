from typing import List
import json

def extend(s:str,l:int,r:int,n:int) -> List[int]:
    while l >= 0 and r <= n-1 and s[l] == s[r]:
        l -= 1
        r += 1
    return [l+1,r-1]

def function(s: str) -> str:
    # 最长回文子串,以当前字符为中心，向两边扩散，遍历一边就能得到最长的回文子串是啥
    n = len(s)
    ans = s[0]
    for i in range(n):
        l1,r1 = extend(s,i,i,n)
        l2,r2 = extend(s,i,i+1,n)
        if r1-l1 > r2-l2:
            if r1-l1+1 > len(ans):
                ans = s[l1:r1+1]
        else:
            if r2-l2+1 > len(ans):
                ans = s[l2:r2+1]
        
    return ans 
    
if __name__ == "__main__":
    print(function(input()))