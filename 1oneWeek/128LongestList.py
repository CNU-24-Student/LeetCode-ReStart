# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度
from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:return 0
        # 核心思想就是哈希记录当前值-1是否存在，如果存在就记录最大值
        nums.sort()
        ans = 1
        cnt = defaultdict(int)
        cnt[nums[0]] = 1  # 第一个元素的值就是存
        for i in range(1,n):
            if cnt[nums[i]-1] > 0:
                cnt[nums[i]] = cnt[nums[i]-1] + 1
                ans = max(ans,cnt[nums[i]])
                continue
            cnt[nums[i]] = 1  # 不连续，那就重新计数
        return ans

    
if __name__ == "__main__":
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    