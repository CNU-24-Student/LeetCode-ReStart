import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = []
        for i in range(n):
            heapq.heappush(h,-nums[i])
        # 构建的是大顶堆，最大的元素在根
        while k > 1:
            heapq.heappop(h)
            k -= 1
        return -h[0]

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    k = int(input())
    s = Solution()
    print(s.findKthLargest(arr,k))