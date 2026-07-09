# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标
from typing import List
from collections import defaultdict

class Solution:
    def function(self,nums:List[int],target:int) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)
        cnt[nums[0]] = 1  # 存下标
        for j in range(1,n):
            if cnt[target-nums[j]] > 0:
                return [cnt[target-nums[j]]-1,j]
            cnt[nums[j]] = j+1
        return [-1,-1]
        
if __name__=="__main__":
    print(Solution().function([2,7,11,15],9))
    # print(Solution().function([3, 1, 4], 6))