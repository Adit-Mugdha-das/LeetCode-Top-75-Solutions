class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        count=0
        l=0
        maxx=0
        for r in range(len(nums)):
            if nums[r]==0:
                count+=1
            if count==2:
                count=1
                l=dic[nums[r]]+1
            maxx=max(maxx,r-l)
            dic[nums[r]]=r
        if count==0:
            return len(nums)-1
        return maxx


'''SOLVED BY ADIT MUGDHA DAS'''