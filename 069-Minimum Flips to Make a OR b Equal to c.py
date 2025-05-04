class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips=0
        for i in range(32):
            bita=(a>>i)&1
            bitb=(b>>i)&1
            bitc=(c>>i)&1
            if (bita|bitb)!=bitc:
                if bitc==1:
                    flips+=1
                else:
                    flips+=bita+bitb 
        return flips
    
'''SOLVED BY ADIT MUGDHA DAS'''