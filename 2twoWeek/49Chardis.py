# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
from typing import List
from collections import defaultdict

class Solution:
    def function(self,strs:List[str]) -> List[List[str]]:
        n = len(strs)
        cnt = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            cnt[sortedS].append(s)
        return list(cnt.values())

if __name__ == "__main__":
    lStr = Solution().function(["eat", "tea", "tan", "ate", "nat", "bat"])
    for l in lStr:
        print(l)