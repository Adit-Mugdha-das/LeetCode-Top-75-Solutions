class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        c=0
        pend=float('-inf')
        for s,e in intervals:
            if s>=pend:
                pend=e
            else:
                c+=1
        return c

'''SOLVED BY ADIT MUGDHA DAS'''