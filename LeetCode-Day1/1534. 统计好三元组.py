# 题目链接：https://leetcode.cn/problems/count-good-triplets/description/?envType=study-plan-v2&envId=primers-list
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if (abs(arr[i] - arr[j])<=a and abs(arr[j] - arr[k])<=b and abs(arr[i] - arr[k])<=c):
                        ans+=1

        return ans

if __name__ == '__main__':
    print(Solution().countGoodTriplets([3,0,1,1,9,7],7,2,3))