from typing import List
import json

def dfs(grid:List[List[int]],x:int,y:int,visit:List[List]) -> None:
    n = len(grid)
    m = len(grid[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
            # 记录需要接下来需要改的位置
            visit.append([nx,ny])


def function(grid:List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    ans = 0
    while True:
        visit = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dfs(grid,i,j,visit)
        if not visit:
            for row in grid:
                if 1 in row:
                    return -1
            return ans
        for x,y in visit:
            grid[x][y] = 2
        ans += 1
    return ans

if  __name__ == "__main__":
    grid = json.loads(input())
    print(grid)
    print(function(grid))
