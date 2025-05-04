class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        vis=[0]*n
        def dfs(x):
            vis[x]=1
            for k in rooms[x]:
                if not vis[k]:
                    dfs(k)
        dfs(0)
        return all(vis)

'''SOLVED BY ADIT MUGDHA DAS'''