# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        psum=defaultdict(int)
        psum[0]=1
        def dfs(node,cursum):
            if not node:
                return 0
            cursum+=node.val
            paths=psum[cursum-targetSum]
            psum[cursum]+=1
            paths+=dfs(node.left,cursum)
            paths+=dfs(node.right,cursum)
            psum[cursum]-=1 
            return paths
        return dfs(root,0)
    
'''SOLVED BY ADIT MUGDHA DAS'''