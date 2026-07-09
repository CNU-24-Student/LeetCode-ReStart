from typing import List
import json
from collections import defaultdict

def function(height:List[int]) -> int:
    ans = 0
    n = len(height)
    l,r = 0,n-1
    while l <= r:
        ans = max(min(height[l],height[r])*(r-l),ans)
        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1
        
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))