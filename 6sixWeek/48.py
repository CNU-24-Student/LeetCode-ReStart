from typing import List
import json

def function(matrix:List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    ans = []
    for i in range(n):
        temp = []
        for j in range(m-1,-1,-1):
            temp.append(matrix[j][i])
        ans.append(temp)
    matrix[:] = ans
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))