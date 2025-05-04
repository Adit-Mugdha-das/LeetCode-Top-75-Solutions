class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        fresh=0
        direc=[(-1, 0),(1, 0),(0, -1),(0, 1)]
        minu=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c,0))  
                elif grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0
        while q:
            r,c,time=q.popleft()
            for dr,dc in direc:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2  
                    fresh-=1
                    q.append((nr,nc,time+1))
                    minu=time+1  
        return -1 if fresh > 0 else minu


'''SOLVED BY ADIT MUGDHA DAS'''