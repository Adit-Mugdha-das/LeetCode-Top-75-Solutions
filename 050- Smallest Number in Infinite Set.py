class SmallestInfiniteSet:

    def __init__(self):
        self.cur=1
        self.adback=set()
        self.mheap=[]

    def popSmallest(self) -> int:
        if self.mheap:
            smal=heapq.heappop(self.mheap)
            self.adback.remove(smal)
            return smal
        else:
            res=self.cur
            self.cur+=1
            return res

    def addBack(self, num: int) -> None:
        if num<self.cur and num not in self.adback:
            heapq.heappush(self.mheap,num)
            self.adback.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

'''SOLVED BY ADIT MUGDHA DAS'''