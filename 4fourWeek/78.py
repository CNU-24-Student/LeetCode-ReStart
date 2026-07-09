# 求子集
from typing import List
import json

def dfs(nums:List[int],ans:List[List[int]],i:int,path:List[int]) -> None:
    ans.append(path[:])
    for i in range(i,len(nums)):
        path.append(nums[i])
        dfs(nums,ans,i+1,path)
        path.pop()

def function(nums:List[int]) -> List[List[int]]:
    ans = []
    dfs(nums,ans,0,[])
    return ans

if __name__ == "__main__":
    nums = json.loads(input())
    print(function(nums))