from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  前 k 高，也需要使用最小堆，最小值
        cnt = defaultdict(int)
        used = set()       # 存的是已经使用过的元素
        ans = []
        h = [] 
        for num in nums: 
            cnt[num] += 1
        # cnt存的是出现次数
        for num,c in cnt.items():
            heapq.heappush(h,-c)  # 维护的也是次数，但是存的是负数，反推大根堆
        
        # 已经构建好了小顶堆
        while k:
            value = -heapq.heappop(h)
            print(value)
            for num,c in cnt.items():
                if c == value and num not in used:
                    ans.append(num)
                    used.add(num)

            k -= 1

        return ans
    
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    k = int(input())
    s = Solution()
    print(s.topKFrequent(arr,k))