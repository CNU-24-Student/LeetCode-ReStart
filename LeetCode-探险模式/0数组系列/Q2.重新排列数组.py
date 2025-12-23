# 题目链接：https://leetcode.cn/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=shujujiegouyusuanfa-xianxingqiantan-shuzu-i
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans += nums[i::n]
        return ans

if __name__ == '__main__':
    ans = Solution().shuffle([2,5,1,3,4,7],3)
    print(ans)