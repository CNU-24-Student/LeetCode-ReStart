from typing import List
import json
from collections import defaultdict

def function(nums:List[int]) -> int:
    n = len(nums)
    ans = 1
    cnt = defaultdict(int)
    maxNum = nums[0]
    for num in nums:
        cnt[num] += 1
        maxNum = max(maxNum,num)
    while ans < maxNum:
        if cnt[ans] == 0:
            return ans
        ans += 1
    if maxNum <= 0: return 1
    return maxNum + 1

if __name__ == "__main__":
    nums = json.loads(input())
    ans = function(nums)
    print(ans)