# 无重复最长子串
from typing import List
import json
import heapq


def function(nums:List[int],k:int) -> List[int]:
    n = len(nums)
    ans = []
    heap = []  # 二维数组（值，下标）
    for i in range(k):
        heapq.heappush(heap,(-nums[i],i)) # heapq默认构建的是小顶堆
    ans.append(-heap[0][0])
    for i in range(k,n):
        heapq.heappush(heap,(-nums[i],i)) # 压进来
        while heap[0][1] <= i-k:
            heapq.heappop(heap)
        ans.append(-heap[0][0])
        
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    k = int(input())
    print(function(arr,k))