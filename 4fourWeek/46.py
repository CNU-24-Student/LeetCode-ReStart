from typing import List
import json

def dfs(nums:List[int],used:List[bool],ans:List[List[int]],path:List[int]) -> None:
    if len(path) == len(nums):
        ans.append(path[:]) # 拷贝path，否则后续修改会影响到已保存的结果
        return
    for i in range(len(nums)):
        if not used[i]:
            path.append(nums[i])
            used[i] = True
            dfs(nums,used,ans,path)
            used[i] = False
            path.pop()
    

def function(nums:List[int]) -> List[List[int]]:
    ans = []
    # 全排列 递归
    used = [False]*len(nums)
    dfs(nums,used,ans,[])
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))