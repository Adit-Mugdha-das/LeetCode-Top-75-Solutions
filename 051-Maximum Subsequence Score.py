class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs=list(zip(nums1,nums2))
        pairs.sort(key=lambda x:-x[1])
        heap=[]
        total=0
        mscore=0
        for n1,n2 in pairs:
            heapq.heappush(heap,n1)
            total+=n1
            if len(heap)>k:
                total-=heapq.heappop(heap)
            if len(heap)==k:
                mscore=max(mscore,total*n2)
        return mscore
    
    '''SOLVED BY ADIT MUGDHA DAS'''