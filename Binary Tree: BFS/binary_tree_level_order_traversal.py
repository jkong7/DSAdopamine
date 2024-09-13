# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        q=deque()
        q.append(root)
        while q: 
            level=[]
            levelcount=len(q)
            for i in range(levelcount): 
                current=q.popleft()
                if current: 
                    level.append(current.val)
                    q.append(current.left)
                    q.append(current.right)
            if level: 
                result.append(level)
        return result 