from typing import List
import json

def function(nums:List[int]) -> int:
    n = len(nums)
    ans = nums[0]
    sum = nums[0]
    for i in range(1,n):
        if sum < 0:
            sum = 0
        sum += nums[i]
        ans = max(sum,ans)
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))