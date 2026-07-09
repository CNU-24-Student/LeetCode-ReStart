from typing import List
class Solution:
    def check(self,Q:List[int],j):
        for i in range(1,j):
            if (Q[i]==Q[j]) or (abs(Q[i]-Q[j])==abs(i-j)):
                return 0
        return 1
    def solveNQueens(self, n: int) -> List[List[str]]:
        Q = [0] * (n+1)
        ans = []
        j = 1
        while j >= 1:
            Q[j] = Q[j]+1
            if Q[j] > n:
                Q[j] = 0
                j -= 1
                continue
            if self.check(Q,j):
                if j == n:
                    cur = []
                    for k in range(1,n+1):
                        s = ["."] * n
                        s[Q[k]-1] = "Q"
                        cur.append("".join(s))
                    ans.append(cur)
                else:
                    j = j + 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))