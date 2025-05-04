class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        row=[tuple(r) for r in grid]
        col=[tuple(grid[r][c] for r in range(n)) for c in range(n)]
        return sum(row.count(c) for c in col)

'''SOLVED BY ADIT MUGDHA DAS'''