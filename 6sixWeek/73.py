from typing import List
import json

def function(matrix:List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    x,y = set(),set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                x.add(i)
                y.add(j)
    for i in range(m):
        for j in range(n):
            if i in x or j in y:
                matrix[i][j] = 0
    return
if __name__ == "__main__":
    arr = json.loads(input())
    function(arr)
    print(arr)