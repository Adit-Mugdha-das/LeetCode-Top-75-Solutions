class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<r:
            k=(l+r)//2
            t=sum((p+k-1)//k for p in piles)
            if t>h:
                l=k+1
            else:
                r=k
        return l

'''SOLVED BY ADIT MUGDHA DAS'''