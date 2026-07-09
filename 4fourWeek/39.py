from typing import List
import json

def dfs(candidates:List[int],start:int,target:int,curSum:int,res:List[List[int]],path:List[int]) -> None:
    if curSum == target:
        res.append(path[:])
    if curSum > target:
        return 
    for i in range(start,len(candidates)):
        if curSum + candidates[i] > target:
            break
        path.append(candidates[i])
        curSum += candidates[i]
        dfs(candidates,i,target,curSum,res,path)
        path.pop()
        curSum -= candidates[i]

def function(candidates:List[int],target:int) -> List[List[int]]:
    candidates.sort()
    res = []
    dfs(candidates,0,target,0,res,[])

    return res

if __name__ == "__main__":
    candidates = json.loads(input())
    target = int(input())
    #  arr = list(map(int,input().split()))
    print(function(candidates,target))