from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while index < n:
            nums[index] = 0
            index += 1

if __name__ == "__main__":
    lNum = [0,1,0,3,12]
    Solution().moveZeroes(lNum)
    print(lNum)