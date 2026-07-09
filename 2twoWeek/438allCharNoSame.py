# 超时！！！！！
# # 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序
# from typing import List
# from collections import defaultdict

# class Solution:
#     def function(self,s:str,p:str) -> List[int]:
#         n = len(s)
#         m = len(p)
#         ans = []
#         cnt_p = defaultdict(int)
#         for ch in p:
#             cnt_p[ch] += 1
#         for i in range(n-m+1):
#             l,r = i,i+m
#             cnt_t = cnt_p.copy()
#             while l < r:
#                 cnt_t[s[l]] -= 1
#                 if cnt_t[s[l]] < 0:
#                     break
#                 l += 1
#             if l == r:
#                 flag = True
#                 for _,value in cnt_t.items():
#                     if value != 0:
#                         flag = False
#                         break
#                 if flag:
#                     ans.append(i)
#         return ans

# if __name__ == "__main__":
#     print(Solution().function("cbaebabacd","abc"))
#     s = input()
#     p = input()
#     print(Solution().function(s,p))

from typing import List
from collections import defaultdict

class Solution:
    def function(self,s:str,p:str) -> List[int]:
        n = len(s)
        m = len(p)
        if n < m: return []
        ans = []
        cnt_p = defaultdict(int)
        cnt_s = defaultdict(int)

        for ch in p:
            cnt_p[ch] += 1

        for i in range(m):
            cnt_s[s[i]] += 1

        if cnt_s == cnt_p:
            ans.append(0)
        l = 0
        for i in range(m,n):
            cnt_s[s[l]] -= 1
            if cnt_s[s[l]] == 0:
                del cnt_s[s[l]]
            l += 1
            cnt_s[s[i]] += 1
            if cnt_s == cnt_p:
                ans.append(i - m + 1)

        return ans


if __name__ == "__main__":
    print(Solution().function("cbaebabacd","abc"))
    s = input()
    p = input()
    print(Solution().function(s,p))