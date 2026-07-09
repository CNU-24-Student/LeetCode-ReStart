# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
from typing import List

class Solution:
    def function(self,height:List[int]) -> int:
        n = len(height)
        ans = 0
        # 遍历1，n-1位置的所有元素
        # 找到左侧，右侧的最大值，然后-当前柱子的高度，最小值取0
        LH ,RH = [0]*n,[0]*n
        for i in range(1,n):
            if height[LH[i-1]] >= height[i]:
                LH[i] = LH[i-1]
            else:
                LH[i] = i

        for j in range(n-1,-1,-1):
            if j == n-1:
                RH[j] = n-1
                continue
            if height[RH[j+1]] >= height[j]:
                RH[j] = RH[j+1]
            else:
                RH[j] = j

        for i in range(1,n-1):
            minH = min(height[LH[i]], height[RH[i]]) - height[i]
            ans += max(0,minH)
                     
        return ans

if __name__=="__main__":
    print(Solution().function([0,1,0,2,1,0,1,3,2,1,2,1]))