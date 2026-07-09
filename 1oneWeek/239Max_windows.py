import heapq
from typing import List
from collections import defaultdict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        heap = []  
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        ans.append(-heap[0][0])

        for j in range(k,n):
            heapq.heappush(heap,(-nums[j],j))
            while heap[0][1] <= j-k:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans