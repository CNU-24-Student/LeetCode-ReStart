# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k 
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组
from typing import List


# nums[i] + nums[j] = -nums[k]
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for k in range(n):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            target = -nums[k]
            l,r = k+1,n-1
            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    ans.append([nums[l],nums[r],nums[k]])
                    while l < r and nums[l] == nums[l+1]:l+=1
                    while l < r and nums[r] == nums[r-1]:r-=1
                    l += 1
                    r -= 1
                
        return ans

if __name__=="__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))