class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n=len(word1),len(word2)
        ns=''.join(w1+w2 for w1,w2 in zip(word1,word2))
        if m>n:
            ns+=word1[n:]
        else:
            ns+=word2[m:]
        return ns
    
'''SOLVED BY ADIT MUGDHA DAS'''