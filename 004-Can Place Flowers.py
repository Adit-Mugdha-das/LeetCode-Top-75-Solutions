class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        leng=len(flowerbed)
        for i in range(leng):
            if flowerbed[i]==0:
                lem=(i==0 or flowerbed[i-1]==0)
                rem=(i==leng-1 or flowerbed[i+1]==0)
                if lem and rem:
                    flowerbed[i]=1
                    c+=1
                    if c>=n:
                        return True
        return c>=n

'''SOLVED BY ADIT MUGDHA DAS'''