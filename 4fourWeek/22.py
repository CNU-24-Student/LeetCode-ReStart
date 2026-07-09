from typing import List
import json


def function(n:int) -> List[List[str]]:
    res = []
    def dfs(path:str,left:int,right:int) -> None:
        if len(path) == 2*n:
            res.append(path)
            return 
        if left < n:
            path += '('
            dfs(path,left+1,right)
            path = path[:-1]
        if right < left:
            path += ')'
            dfs(path,left,right+1)
            path = path[:-1]
            
    dfs('',0,0)
    return res

if __name__ == "__main__":
    n = int(input())
    print(function(n))