from typing import List
import json
from collections import defaultdict

def function(nums:List[List[int]]) -> None:
    m = len(nums)
    n = len(nums[0])
    cnt_row = defaultdict(int)
    cnt_col = defaultdict(int)
    for row in range(m):
        for col in range(n):
            if nums[row][col] == 0:
                cnt_row[row] += 1
                cnt_col[col] += 1
    for row in range(m):
        for col in range(n):
            if cnt_row[row] > 0 or cnt_col[col] > 0:
                nums[row][col] = 0
    # print(nums)

if __name__ == "__main__":
    userinput = input()
    nums = json.loads(userinput)
    function(nums)
    # 直接输出 nums  [[1,1,1],[1,0,1],[1,1,1]]
    print(nums)