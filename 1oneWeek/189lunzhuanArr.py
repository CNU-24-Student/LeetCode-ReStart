from typing import List
import json

def function(nums:List[int],k:int) -> None:
    n = len(nums)
    k = k % n
    if k == n:return 
    temp = []
    left,right = 0,0
    while right < n-k:
        temp.append(nums[right])
        right += 1
    while right < n:
        nums[left] = nums[right]
        left += 1
        right += 1
    i = 0
    while left < n:
        nums[left] = temp[i]
        i += 1
        left += 1
    return 

if __name__ == "__main__":
    # nums = list(map(int,input().split()))
    # k = int(input())
    # function(nums,k)
    # # 如何输出：[5,6,7,1,2,3,4]
    # print(','.join(str(num) for num in nums))
    userinput = input()
    nums = json.loads(userinput)
    k = int(input())
    function(nums,k)
    print(','.join(str(num) for num in nums))