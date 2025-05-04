# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        mx,lvl,res,cur=float('-inf'),1,1,1
        while q:
            s=0
            for i in range(len(q)):
                n=q.popleft()
                s+=n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if s>mx:
                mx,res=s,cur
            cur+=1
        return res
    
'''SOLVED BY ADIT MUGDHA DAS'''