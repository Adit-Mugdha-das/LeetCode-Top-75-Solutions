class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])
        q=deque()
        q.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]]='+'
        d=[(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            x,y,s=q.popleft()
            for dx,dy in d:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and maze[nx][ny]=='.':
                    if nx==0 or nx==m-1 or ny==0 or ny==n-1:
                        return s+1
                    maze[nx][ny]='+'
                    q.append((nx,ny,s+1))
        return -1


'''SOLVED BY ADIT MUGDHA DAS'''