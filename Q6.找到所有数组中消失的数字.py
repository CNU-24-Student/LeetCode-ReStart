# 题目链接：https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/?envType=problem-list-v2&envId=shujujiegouyusuanfa-xianxingqiantan-shuzu-ii
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash = [0]*(n+1)
        ans = []

        for i,num in enumerate(nums):
            hash[num]+=1
        for i  in range(1,n+1):
            if hash[i] == 0: ans.append(i)
        return ans

if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))