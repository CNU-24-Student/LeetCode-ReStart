# 分割回文串
# 分割后的子串全部都是回文串

from typing import List
import json

def is_palindrome(sub:str) -> bool:
    return sub == sub[::-1]

def function(s:str) -> List[List[str]]:
    if not s: return []
    n = len(s)

    ans = []
    path = []

    def backtrack(start:int) -> None:
        if start == n:
            ans.append(path[:])
            return
        for end in range(start,n):
            sub = s[start:end+1]
            if is_palindrome(sub):
                path.append(sub)
                backtrack(end+1)
                path.pop()
    backtrack(0)
    return ans

if __name__ == "__main__":
    arr = input()
    print(function(arr))