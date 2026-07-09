from typing import defaultdict

class Solution:
    def function(self,s:str) -> int:
        n = len(s)
        if n <= 1 : return n
        ans = 1
        l,r = 0,1
        cnt = defaultdict(int)
        cnt[s[0]] = 1
        while r < n:
            while l < r and cnt[s[r]] > 0:
                cnt[s[l]] -= 1
                l += 1
            if l < r:
                ans = max(ans,r-l+1)
            cnt[s[r]] += 1
            r += 1
        return ans

if __name__ == "__main__":
    print(Solution().function("abcabcbb"))
    print(Solution().function("bbb"))
    print(Solution().function("pwwkew"))