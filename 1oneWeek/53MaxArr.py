from typing import List
class Solution:
    def function(self,nums:List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        val = 0
        for i in range(n):
            val += nums[i]
            ans = max(ans,val)
            if val < 0:val = 0
                
        return ans

if __name__=="__main__":
    print(Solution().function([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().function([1]))
    print(Solution().function([5,4,-1,7,8]))
    print(Solution().function([-2,-1]))