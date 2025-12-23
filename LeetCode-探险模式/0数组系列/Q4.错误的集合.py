# 题目链接：https://leetcode.cn/problems/set-mismatch/description/?envType=problem-list-v2&envId=shujujiegouyusuanfa-xianxingqiantan-shuzu-ii
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash = [0] * (n+1)
        ans = []
        for i in nums:
            if hash[i] == 0:
                hash[i] = 1
            else: ans.append(i)
        for i in range(1,n+1):
            if hash[i] == 0:
                ans.append(i)
        return ans

if __name__ == "__main__":
    print(Solution().findErrorNums([1,2,2,4]))