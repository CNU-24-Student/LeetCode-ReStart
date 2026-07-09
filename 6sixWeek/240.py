from typing import List
import json

def function(matrix:List[List[int]],target:int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    # 先快速定位到哪一行？或者哪一列，然后二分查找
    for col in matrix:
        x = len(col)
        l,r = 0,x-1
        if col[0] > target:
            break
        while l <= r:
            mid = (l+r)//2
            if col[mid] == target:
                return True
            elif col[mid] > target:
                r = mid-1
            else:
                l = mid+1
    return False

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr,int(input())))