# 题目链接：https://leetcode.cn/problems/root-equals-sum-of-children/description/?envType=study-plan-v2&envId=primers-list
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return True if (root.right.val+root.left.val==root.val) else False


if __name__ == '__main__':
    print(Solution().checkTree(TreeNode(10,TreeNode(4),TreeNode(6))))