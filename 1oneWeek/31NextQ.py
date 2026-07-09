from typing import List

class Solution:
    def function(self,nums:List[int]) -> None:
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i < 0:
            nums.reverse()
            return 

        for j in range(n-1,i,-1):
            if nums[j] > nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                # 交换后，后续i之后的所有元素直接反转
                # nums[i:].reverse()   这是创建副本，不会修改原数组
                # nums[i+1:] = reversed(nums[i+1:])
                nums[i+1:] = nums[i+1:][::-1]
                break
        return 
            
        
if __name__ == "__main__":
    nums = list(map(int,input().split()))
    print(Solution().function(nums))
    print(nums)  # 打印后的结果就是[1,2,3]
    print(f"[{', '.join(map(str, nums))}]")  # 自定义打印格式 
    for num in nums:
        print(num)