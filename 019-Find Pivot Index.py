class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tsum=sum(nums)
        lsum=0
        for i,n in enumerate(nums):
            if lsum==tsum-lsum-n:
                return i
            lsum+=n        
        return -1

'''SOLVED BY ADIT MUGDHA DAS'''