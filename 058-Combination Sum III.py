class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        can=[1,2,3,4,5,6,7,8,9]
        res=[]
        def backtrack(i,cur,total):
            if total==n and len(cur)==k:
                res.append(cur.copy())
                return
            if total>n or len(cur)>k or i>=len(can):
                return
            cur.append(can[i])
            backtrack(i+1,cur,total+can[i])
            cur.pop()
            backtrack(i+1,cur,total)
        backtrack(0,[],0)
        return res
    
'''SOLVED BY ADIT MUGDHA DAS'''