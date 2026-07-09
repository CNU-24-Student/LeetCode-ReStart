# 给你一个字符串 s，找到 s 中最长的 回文 子串
# 最长回文，中间值为中心，left = right
from typing import List

class Solution:
    def function(self,s:str) -> str:
        n = len(s)
        ans = s[0]
        def extend(left:int,right:int) -> List[int]:
            while left>=0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return [left+1,right-1]
        for i in range(n):
            l1,r1 = extend(i,i)
            l2,r2 = extend(i,i+1)
            print(l1,r1,l2,r2)
            if r1-l1 > r2-l2:
                if r1-l1+1 > len(ans):
                    ans = s[l1:r1+1]
            else:
                if r2-l2+1 > len(ans):
                    ans = s[l2:r2+1]
        return ans
            
if __name__=="__main__":
    print(Solution().function("babad"))
            