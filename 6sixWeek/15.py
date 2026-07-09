from typing import List
import json
from collections import defaultdict

def function(nums:List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    # 是否存在三元组，ijk，满足nums[i] + nums[j] + nums[k] == 0
    # 问题切换：nums[i] + nums[j] == -nums[k]
    ans = []
    for k in range(n-2):
        if k > 0 and nums[k] == nums[k-1]:
            continue
        target = -nums[k]
        # 剪枝+两数之和=target
        seen = set()  # 存储已经遍历过的数字
        i = k + 1
        while i < n:
            cur = target - nums[i]
            if cur in seen:
                ans.append([nums[k], cur, nums[i]])
                # 跳过后续相同的 nums[i]
                while i + 1 < n and nums[i + 1] == nums[i]:
                    i += 1
            seen.add(nums[i])
            i += 1
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))