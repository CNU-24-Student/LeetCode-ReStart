# 题目链接：https://leetcode.cn/problems/number-of-good-pairs/description/?envType=study-plan-v2&envId=primers-list
from typing import List


# 思路1：暴力
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         ans = 0
#         for i,num1 in enumerate(nums):
#             for j,num2 in enumerate(nums):
#                 if i < j and num1 == num2:
#                     ans += 1
#         return ans

# 思路2：哈希计数
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        ans = 0
        for num in nums:
            hash[num] = hash.get(num,0) + 1
        for cnt in hash.values():
            ans = ans+(cnt*(cnt-1)//2)
        return ans
if __name__ == "__main__":
    print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
