# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque 
        maxsum=float('-inf')
        q=deque([root])
        level=0 
        result=0 
        while q: 
            levelsum=0 
            level+=1 
            for _ in range(len(q)): #Distinguishes between levels-"do something" at each level
                current=q.popleft()
                if current: 
                    levelsum+=current.val 
                    if current.left: 
                        q.append(current.left)
                    if current.right: 
                        q.append(current.right)
            if levelsum>maxsum: 
                maxsum=levelsum
                result=level 
        return result 



        maxlevelsum=float('-inf')
        level=0 
        result=0 
        q=deque([root])
        while q: 
            levelsum=0 
            level+=1 
            for _ in range(len(q)): 
                current=q.popleft()
                levelsum+=current.val
                if current.left: 
                    q.append(current.left)
                if current.right: 
                    q.append(current.right)
            if levelsum>maxlevelsum: 
                maxlevelsum=levelsum
                result=level 
        return result

        #Level order iterating and summing levels and keeping track of 
        #max. If that max value has already been seen, don't update the result level
        #instead just stop and continue to next for loop iteration/level 
       