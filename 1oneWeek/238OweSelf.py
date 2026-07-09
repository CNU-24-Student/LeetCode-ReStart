from typing import List
import json

def function(nums:List[int]) -> List[int]:
    n = len(nums)
    leftArr,rightArr = [1]*n,[1]*n
    ans = []
    SUM = nums[0]
    for i in range(1,n):
        leftArr[i] = SUM
        SUM *= nums[i]
    # leftArr存的该元素所有左侧累乘的值

    SUM = nums[n-1]
    for j in range(n-2,-1,-1):
        rightArr[j] = SUM
        SUM *= nums[j]
    # rightArr存的该元素所有右侧累乘的值
    for i in range(n):
        ans.append(leftArr[i]*rightArr[i])

    return ans

if __name__ == "__main__":
    # nums = list(map(int,input().split()))
    # arr = function(nums)
    arr = input()
    arr = json.loads(arr)
    arr = function(arr)
    print(",".join(str(num) for num in arr))