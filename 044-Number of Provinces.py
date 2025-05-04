class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        vis=[0]*n
        c=0
        def dfs(i):
            vis[i]=1
            for j in range(n):
                if isConnected[i][j]==1 and not vis[j]:
                    dfs(j)
       
        for i in range(n):
            if not vis[i]:
                dfs(i)
                c+=1
        return c

'''SOLVED BY ADIT MUGDHA DAS'''