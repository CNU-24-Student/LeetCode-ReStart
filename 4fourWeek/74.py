# 查target，每行内部使用二分查找，每列通过查左+右
from typing import List
import json

def function(matrix:List[List[int]],target:int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        left = matrix[i][0]
        right = matrix[i][n-1]
        if target >= left and target <= right:
            if target == left or target==right:
                return True
            l,r = 0,n-1
            while l < r:
                mid = (l+r)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r = mid
                elif matrix[i][mid] < target:
                    l = mid+1    
    return False

if __name__ == "__main__":
    arr = json.loads(input())
    target = int(input())
    print(function(arr,target))