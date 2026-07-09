from typing import List
import json

class Solution:
    def function(self,matrix:List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        cnt = m*n
        ans = []
        i,j = 0,0
        quan = 0
        while cnt > 0:
            while cnt and j < n-quan:
                ans.append(matrix[i][j])
                j += 1
                cnt -= 1 
            j -= 1 
            i += 1
            while cnt and i < m-quan:
                ans.append(matrix[i][j])
                i += 1
                cnt -= 1
            i -= 1
            j -= 1
            while cnt and j >= quan:
                ans.append(matrix[i][j])
                j -= 1
                cnt -= 1
            j += 1
            i -= 1
            while cnt and i > quan:
                ans.append(matrix[i][j])
                i -= 1
                cnt -= 1
            i += 1
            j += 1
            quan += 1
        return ans

if __name__ == "__main__":
    userInput = input()
    matrix = json.loads(userInput)
    ans = Solution().function(matrix)
    print([",".join(str(num) for num in ans)])
    