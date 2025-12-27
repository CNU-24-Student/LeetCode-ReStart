# 题目链接：https://leetcode.cn/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1,n):
            ans = ans^(start+2*i)
        return ans

if __name__ == '__main__':
        print(Solution().xorOperation(5,0))
