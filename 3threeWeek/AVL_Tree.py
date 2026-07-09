import json

class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # 节点高度（叶子节点高度为1）

def get_height(node):
    """获取节点高度"""
    if not node:
        return 0
    return node.height

def update_height(node):
    """更新节点高度"""
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    """获取平衡因子（左子树高度 - 右子树高度）"""
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    """右旋转（处理左左情况）"""
    x = y.left
    T2 = x.right
    
    # 执行旋转
    x.right = y
    y.left = T2
    
    # 更新高度
    update_height(y)
    update_height(x)
    
    return x  # 返回新的根节点

def left_rotate(x):
    """左旋转（处理右右情况）"""
    y = x.right
    T2 = y.left
    
    # 执行旋转
    y.left = x
    x.right = T2
    
    # 更新高度
    update_height(x)
    update_height(y)
    
    return y  # 返回新的根节点

def insert(root, val):
    """向AVL树中插入一个值"""
    # 1. 普通BST插入
    if not root:
        return AVLNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    else:
        # 重复值不插入（可根据需求修改）
        return root
    
    # 2. 更新当前节点高度
    update_height(root)
    
    # 3. 获取平衡因子
    balance = get_balance(root)
    
    # 4. 四种不平衡情况处理
    
    # 左左情况：balance > 1 且 val < root.left.val
    if balance > 1 and val < root.left.val:
        return right_rotate(root)
    
    # 右右情况：balance < -1 且 val > root.right.val
    if balance < -1 and val > root.right.val:
        return left_rotate(root)
    
    # 左右情况：balance > 1 且 val > root.left.val
    if balance > 1 and val > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    # 右左情况：balance < -1 且 val < root.right.val
    if balance < -1 and val < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

def build_avl_tree(arr):
    """从数组构建AVL树"""
    if not arr:
        return None
    
    root = None
    for val in arr:
        root = insert(root, val)
    return root

def print_tree(root, level=0, prefix="根: "):
    """可视化打印AVL树（树形结构）"""
    if not root:
        return
    
    if root.left or root.right:
        if root.left:
            print_tree(root.left, level + 1, "L: ")
        else:
            print("  " * (level + 1) + "L: None")
        if root.right:
            print_tree(root.right, level + 1, "R: ")
        else:
            print("  " * (level + 1) + "R: None")


def main():
    arr = json.loads(input().strip())
    # 构建AVL树
    root = build_avl_tree(arr)
    # 打印AVL树结构
    print_tree(root)

if __name__ == "__main__":
    main()