# 题目链接：https://leetcode.cn/problems/max-consecutive-ones/?envType=problem-list-v2&envId=shujujiegouyusuanfa-xianxingqiantan-shuzu-i
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = count = 0
        for index, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                maxcount = max(maxcount, count)
                count = 0
        maxcount = max(maxcount, count)
        return maxcount

if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))