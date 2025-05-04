class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num=max(candies)
        n=len(candies)
        res=[True]*n
        for i in range(n):
            if (candies[i]+extraCandies)<max_num:
                res[i]=False
            
        return res
            
            
'''SOLVED BY ADIT MUGDHA DAS'''