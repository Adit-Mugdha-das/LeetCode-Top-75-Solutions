class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Returns the maximum number of operations that can be performed.
        """
        nums.sort()
        l,r=0,len(nums)-1
        op=0
        while l<r:
            total=nums[l]+nums[r]
            if total==k:
                op+=1
                l+=1
                r-=1  
            elif total<k:
                l+=1  
            else:
                r-=1  
        return op

'''SOLVED BY ADIT MUGDHA DAS'''