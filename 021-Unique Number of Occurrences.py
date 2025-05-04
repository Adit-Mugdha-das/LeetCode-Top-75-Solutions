class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=Counter(arr)
        return len(set(freq.values()))==len(freq.values())


'''SOLVED BY ADIT MUGDHA DAS'''