class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        col = []  # 列元素 
        row = []  # 行元素
        i,j = 0,0
        for i in range(m):
            flag = False
            for j in range(n):
                if matrix[i][j] == target:
                    flag = True
                    break 
            if flag:
                break
        if i == m-1 and j == n-1 and matrix[i][j] != target: return False
        for k in range(m):
            for y in range(n):
                if k == i:
                    # 同一行
                    if len(col) == 0:col.append(matrix[i][j])
                    elif matrix[i][j] < col[-1]: return False
                    else: col.append(matrix[i][j])
                if y == j:
                    # 同一列
                    if len(row) == 0:row.append(matrix[i][j])
                    elif matrix[i][j] < row[-1]: return False
                    else: row.append(matrix[i][j])
                    
        return True