class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)
        total=0
        left,right=[],[]
        l,r=0,n-1
        while l<=r and len(left)<candidates:
            heappush(left,(costs[l],l))
            l+=1
        while r>=l and len(right)<candidates:
            heappush(right,(costs[r],r))
            r-=1
        for i in range(k):
            if right and (not left or right[0][0]<left[0][0]):
                cost,idd=heappop(right)
                total+=cost
                if r>=l:
                    heappush(right,(costs[r],r))
                    r-=1
            else:
                cost,idd=heappop(left)
                total+=cost
                if l<=r:
                    heappush(left,(costs[l],l))
                    l+=1
        return total


'''SOLVED BY ADIT MUGDHA DAS'''