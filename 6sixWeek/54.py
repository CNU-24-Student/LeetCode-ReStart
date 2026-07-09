from typing import List
import json

def function(matrix:List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    ans = []
    i,j = 0,0
    quan = 0
    cnt = 0
    while cnt < m*n:
        while cnt < m*n and j < n-quan:
            ans.append(matrix[i][j])
            j += 1
            cnt += 1
        j -= 1
        i += 1
        
        # 🔥 改动1：如果 cnt 已达目标，直接 break
        if cnt >= m*n:
            break
            
        while cnt < m*n and i < m-quan:
            ans.append(matrix[i][j])
            i += 1
            cnt += 1
        i -= 1
        j -= 1
        
        # 🔥 改动2：如果 cnt 已达目标，直接 break
        if cnt >= m*n:
            break
            
        while cnt < m*n and j >= 0+quan:
            ans.append(matrix[i][j])
            j -= 1
            cnt += 1
        j += 1
        i -= 1
        quan += 1
        
        # 🔥 改动3：如果 cnt 已达目标，直接 break
        if cnt >= m*n:
            break
            
        while cnt < m*n and i >= 0+quan:
            ans.append(matrix[i][j])
            i -= 1
            cnt += 1
        i += 1
        j += 1
        
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))