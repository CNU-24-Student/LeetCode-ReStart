# 电话字母组合
from typing import List
import json

DIGIT_MAP = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz",
}
def dfs(digitStr:List[str],n:int,index:int,ans:List[str],path:str) -> None:
    if len(path) == n:
        ans.append(path[:])
        return
    for ch in digitStr[index]:
        path+=ch
        dfs(digitStr,n,index+1,ans,path)
        path = path[:-1]

def function(digits:str) -> List[str]:
    ans = []
    # 输入的是数字，输出的是对应的组合
    digitStr = []
    for i in range(len(digits)):
        digitStr.append(DIGIT_MAP[digits[i]])
    dfs(digitStr,len(digits),0,ans,"")
    return ans

if __name__ == "__main__":
    arr = input()
    print(function(arr))