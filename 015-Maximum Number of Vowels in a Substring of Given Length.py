class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel='aeiou'
        subaray=list(s[:k])
        maxx=0
        
        for i in subaray:
            if i in vowel:
                maxx+=1
        total=maxx
        for i in range(k,len(s)):
            if s[i] in vowel:
                total+=1
            if s[i-k] in vowel:
                total-=1
            if total>maxx:
                maxx=total
        return maxx

'''SOLVED BY ADIT MUGDHA DAS'''