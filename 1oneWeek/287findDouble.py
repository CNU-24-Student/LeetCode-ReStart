# # 要求O(1)、不修改nums
# from typing import List
# from collections import defaultdict

# class Solution:
#     def function(self,nums:List[int]) -> int:
#         n = len(nums)
#         cnt = defaultdict(int)
#         for num in nums:
#             if cnt[num] > 0:
#                 return num
#             cnt[num] += 1
#         return -1

# if __name__ == "__main__":
#     nums = list(map(int,input().split()))
#     print(Solution().function(nums))


# 仅适用于只有一个数字重复两次
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         n = len(nums)-1
#         # 数学题
#         sum = 0
#         for num in nums:
#             sum += num
#         return sum - n*(n+1)//2


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = 0
        bit = 1
        
        while bit <= n:
            expected = 0
            actual = 0
            
            for num in nums:
                if num & bit:
                    actual += 1
            for i in range(1, n + 1):
                if i & bit:
                    expected += 1
            
            if actual > expected:
                res |= bit
            
            bit <<= 1
        
        return res

