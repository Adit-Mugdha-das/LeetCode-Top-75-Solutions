class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        maxx=0
        zero=0
        for r,num in enumerate(nums)           :
            if num!=1:
                zero+=1
            while zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            maxx=max(maxx,r-l+1)
        return maxx
    
    '''SOLVED BY ADIT MUGDHA DAS'''