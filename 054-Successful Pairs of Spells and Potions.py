class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        m=len(potions)
        for s in spells:
            minp=(success+s-1)//s
            i=bisect_left(potions, minp)
            res.append(m-i)
        return res


'''SOLVED BY ADIT MUGDHA DAS'''