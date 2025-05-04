class Solution:
    def compress(self, chars: List[str]) -> int:
        w=0
        r=0
        n=len(chars)
        while r<n:
            char=chars[r]
            c=0
            while r<n and chars[r]==char:
                r+=1
                c+=1
            chars[w]=char
            w+=1
            if c>1:
                for i in str(c):
                    chars[w]=i
                    w+=1
        return w

'''SOLVED BY ADIT MUGDHA DAS'''