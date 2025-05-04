# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(n,d,l):
            if not n:
                return
            self.res=max(self.res,l)
            if d==0:
                dfs(n.left,1,l+1)
                dfs(n.right,0,1)
            else:
                dfs(n.right,0,l+1)
                dfs(n.left,1,1)
        dfs(root.left,1,1)
        dfs(root.right,0,1)
        return self.res

'''SOLVED BY ADIT MUGDHA DAS'''