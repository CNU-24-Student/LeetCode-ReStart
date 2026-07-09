from typing import List
import json

def function(nums1:List[int],nums2:List[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    all = []
    l1,l2=0,0
    while l1 < n1 and l2 < n2:
        if nums1[l1] <= nums2[l2]:
            all.append(nums1[l1])
            l1 += 1
        else:
            all.append(nums2[l2])
            l2 += 1
    while l1 < n1:
        all.append(nums1[l1])
        l1 += 1
        
    while l2 < n2:
        all.append(nums2[l2])            
        l2 += 1
    # print(all)
    x = n1 + n2
    mid = x // 2
    if x %2 == 0: # 是偶数
        return (all[mid-1] + all[mid]) /2
    return float(all[mid])

if __name__ == "__main__":
    nums1 = json.loads(input())
    nums2 = json.loads(input())
    print(function(nums1,nums2))