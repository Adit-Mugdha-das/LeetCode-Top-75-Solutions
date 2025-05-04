class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total=sum(nums[:k])
        maxx=total
        for i in range(k,len(nums)):
            total+=nums[i]
            total-=nums[i-k]
            if total>maxx:
                maxx=total
        return maxx/k
    
'''SOLVED BY ADIT MUGDHA DAS'''