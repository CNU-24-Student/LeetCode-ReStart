from typing import List
from collections import defaultdict

class Solution:
    def function(self,nums:List[int],k:int) -> int:
        n = len(nums)
        ans = 0
        # 和为k，也就是说我遍历当前元素的时候，我先用k-当前元素，然后查看cnt中是否有，如果有那就+1
        cnt = defaultdict(int)
        cnt[0] = 1  # 如果当前元素就等于k的话，那就k-当前元素 = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            ans += cnt[sum-k]
            cnt[sum] += 1
        return ans

if __name__=="__main__":
    
    nums = list(map(int,input().split()))
    k = int(input())
    print(Solution().function(nums,k))