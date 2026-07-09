from typing import List
import json

class Solution:
    def dfs(self,grid:List[List[str]],x:int,y:int) -> None:
        # 上下左右
        dx = [-1,1,0,0] 
        dy = [0,0,-1,1]
        n = len(grid)
        m = len(grid[0])
        if x<0 or x >= n or y < 0 or y >= m or grid[x][y] == '0':
            return 
        grid[x][y] = '0' # 当前传入的设置为0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            self.dfs(grid,nx,ny)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt +=1
                    self.dfs(grid,i,j)
        return cnt

if __name__ == "__main__":
    grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
    print(Solution().numIslands(grid))
    print(grid)