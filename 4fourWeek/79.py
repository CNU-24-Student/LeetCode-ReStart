from typing import List
import json


def function(board:List[List[int]],word:str) -> bool:
    # 判断当前单元格中的元素实是否可以通过相连的拼接
    # 1、先匹配到第一个单词的位置，然后依次上下左右匹配
    if not word:return True
    if not board: return False
    m = len(board)
    n = len(board[0])
    used = [[0]*n for _ in range(m)]
    def havingWord(x:int,y:int,index:int) -> bool:
        if index == len(word): return True 
        if x < 0 or x >= m or y < 0 or y >=n or used[x][y]==1 or word[index]!=board[x][y]:
            return False
        used[x][y] = 1
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if havingWord(nx,ny,index+1):
                return True
        used[x][y] = 0
        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]: # 这是第一个单词匹配的位置
                if havingWord(i,j,0) == True:return True
    return False

if __name__ == "__main__":
    arr = json.loads(input())
    word = input()
    print(function(arr,word))    