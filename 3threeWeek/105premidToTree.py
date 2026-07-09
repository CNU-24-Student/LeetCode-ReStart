class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        # 从中序中找根节点
        l = 0
        while l < len(inorder) and inorder[l] != preorder[0]:
            l += 1

        if l == 0:root.left = None
        else:root.left = self.buildTree(preorder[1:l+1],inorder[:l])
        if len(preorder) <= l+1 or len(inorder) <= l+1: root.right = None
        else:root.right = self.buildTree(preorder[l+1:],inorder[l+1:])

        return root