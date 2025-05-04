class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt,malt=0,0
        for g in gain:
            alt+=g
            malt=max(malt,alt)
        return malt

'''SOLVED BY ADIT MUGDHA DAS'''