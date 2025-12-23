# 题目链接：https://leetcode.cn/problems/build-an-array-with-stack-operations/description/?envType=problem-list-v2&envId=shujujiegouyusuanfa-xianxingqiantan-zhan
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        size = len(target)
        cur = 1
        ans = []
        i = 0
        while i < size:
            while i<size and target[i] == cur:
                ans.append("Push")
                cur+=1
                i+=1
            if i<size and target[i] != cur:
                cur+=1
                ans.append("Push")
                ans.append("Pop")
        return ans

if __name__ == "__main__":
    target = [1,3]
    n = 3
    s = Solution()
    ans = s.buildArray(target, n)
    print(ans)