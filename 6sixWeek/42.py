# # 超时
# from typing import List
# import json

# def function(height:List[int]) -> int:
#     n = len(height)
#     ans = 0
#     # 第一个和最后一个不计算
#     # 从第二个开始计算，以当前柱子为标准，找到左侧最大和右侧最大，计算 次大；次大的值-当前竹子的值就是当前柱子可以存的水
#     for i in range(1,n-1):
#         cur = height[i]
#         l,r = i-1,i+1
#         lH,rH = cur,cur
#         while l >= 0:
#             lH = max(height[l],lH)
#             l -= 1
#         while r <= n-1:
#             rH = max(height[r],rH)
#             r += 1
#         Theight = min(lH,rH)
#         ans += 0 if Theight <= cur else Theight-cur
            
#     return ans


# if __name__ == "__main__":
#     arr = json.loads(input())
#     print(function(arr))



from typing import List
import json

def function(height:List[int]) -> int:
    n = len(height)
    ans = 0
    # 每次记录当前位置的左侧最大值和右侧最大值
    # 两次for循环记录
    Lheight = [0]*n
    Rheight = [0]*n
    for i in range(1,n):
        Lheight[i] = max(Lheight[i-1],height[i-1])
    for j in range(n-2,-1,-1):
        Rheight[j] = max(Rheight[j+1],height[j+1])
    print(Lheight,Rheight)
    for i in range(1,n-1):
        Theight = min(Lheight[i],Rheight[i])
        ans += 0 if Theight <= height[i] else Theight-height[i]
            
    return ans


if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))