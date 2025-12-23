# 题目链接：https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/description/?envType=problem-list-v2&envId=shujujiegouyusuanfa-xianxingqiantan-shuzu-ii
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i, numi in enumerate(nums):
            count = 0
            for j, numj in enumerate(nums):
                if i == j: continue
                if numj < numi:
                    count += 1
            ans.append(count)
        return ans

if __name__ == '__main__':
    print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
