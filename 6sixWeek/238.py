from typing import List
import json

def function(nums:List[int]) -> List[int]:
    n = len(nums)
    pre = [1]*n
    suf = [1]*n
    for i in range(1,n):
        pre[i] = pre[i-1]*nums[i-1]
    for j in range(n-2,-1,-1):
        suf[j] = suf[j+1]*nums[j+1]
    ans = []
    for i in range(n):
        ans.append(pre[i]*suf[i])
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))