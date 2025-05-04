class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g=defaultdict(list)
        for a,b in connections:
            g[a].append((b,1))
            g[b].append((a,0))
        vis=[0]*n
        res=0
        def dfs(u):
            nonlocal res
            vis[u] = 1
            for v,n in g[u]:
                if not vis[v]:
                    res+=n
                    dfs(v)
        dfs(0)
        return res

'''SOLVED BY ADIT MUGDHA DAS'''