# 无重复最长子串
from typing import List
import json
from collections import defaultdict


def function(nums:List[int],k:int) -> int:
    n = len(nums)
    ans = 0
    # 和为k
    sum = 0
    cnt = defaultdict(int)
    cnt[0] = 1
    for num in nums:
        sum += num
        ans += cnt[sum-k]
        cnt[sum] += 1

    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    k = int(input())
    print(function(arr,k))