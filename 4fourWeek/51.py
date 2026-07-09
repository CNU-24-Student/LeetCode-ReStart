# N皇后
# 条件：同一行，同一列不能出现第二个皇后
# 维护一个d[i]数组，表示第i行的第d[i]个位置放了皇后
from typing import List
import json

def check(d:List[int],j:int) -> int:
    for i in range(1,j):
        if d[i] == d[j] or (abs((i-j))==abs(d[i]-d[j])):
            return 0
    return 1
    
def function(m:int) -> List[List[int]]:
    ans = []
    d = [0]*(m+1) # 第一行用1存
    j = 1
    while j >= 1:
        d[j] = d[j] + 1
        if d[j] > m:
            d[j] = 0
            j = j-1
            continue
        if check(d,j) == 1:
            if j == m:
                cur = []
                for k in range(1,m+1):
                    s = ["."]*m
                    s[d[k]-1] = "Q"
                    s = "".join(s)
                    cur.append(s)
                ans.append(cur)
            else:
                j = j+1
    return ans
    return ans

if __name__ == "__main__":
    arr = int((input()))
    print(function(arr))