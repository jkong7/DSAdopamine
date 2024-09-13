# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque 
        result=[]
        q=deque([root])
        while q: 
            level=0 
            numberofnodes=0 
            for _ in range(len(q)): 
                current=q.popleft()
                level+=current.val 
                numberofnodes+=1 
                if current:
                    q.append(current.left) if current.left else None
                    q.append(current.right) if current.right else None
            result.append(level/float(numberofnodes))
        return result 

        #Level order, iterating through level nodes and taking average. Just need a 
        #reset before each for loop/level. Don't queue null nodes.