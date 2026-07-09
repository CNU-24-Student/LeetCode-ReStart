from typing import List
from collections import defaultdict

class Solution:
    def function(self,nums:List[int]) -> None:
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i],nums[index] = nums[index],nums[i]
                index += 1
        for i in range(index,n):
            if nums[i] == 1:
                nums[i],nums[index] = nums[index],nums[i]
                index += 1

if __name__ == "__main__":
    nums = list(map(int,input().split()))
    print(Solution().function(nums))
    for num in nums:
        print(num)