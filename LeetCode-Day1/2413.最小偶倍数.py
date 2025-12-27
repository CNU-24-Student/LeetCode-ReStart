# 题目链接：https://leetcode.cn/problems/smallest-even-multiple/description/?envType=study-plan-v2&envId=primers-list

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2==0 else n*2

if __name__ =='__main__':
    print(Solution().smallestEvenMultiple(6))