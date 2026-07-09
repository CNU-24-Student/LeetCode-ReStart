from typing import List
import json

def function(intervals:List[int]) -> List[List[int]]:
    n = len(intervals)
    ans = []
    # 对数组的第一个进行排序
    intervals.sort(key=lambda x: x[0]) # 等价于一个函数
    l,r = intervals[0][0],intervals[0][1]
    for i in range(1,n):
        if r >= intervals[i][0]:
            r = max(r,intervals[i][1])
        else:
            ans.append([l,r])
            l,r = intervals[i][0],intervals[i][1]
    ans.append([l,r])
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))