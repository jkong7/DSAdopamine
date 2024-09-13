# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Should be level order, all the deepest leaves will be on the same level
        #If at any level, there IS a node with children, its not the deepest level
        from collections import deque 
        q=deque([root])
        while q: 
            notYet=False
            levelsum=0 
            for _ in range(len(q)): 
                current=q.popleft()
                levelsum+=current.val
                if current.left: 
                    notYet=True 
                    q.append(current.left)
                if current.right: 
                    notYet=True
                    q.append(current.right)
            if not notYet: 
                return levelsum
        return -1
