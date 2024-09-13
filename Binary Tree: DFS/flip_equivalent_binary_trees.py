# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2: 
            return True 
        if not root1 or not root2: 
            return False
        if root1.val!=root2.val: 
            return False 
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

        #Structure: Series of false checks as go down. If 
        #passes all of them, then at the end, return True (if not r1 and not r2)
        #At each node, if one missing or vals are diff, return false (check for 
        #sameness). Then, that same check for sameness has to pass for either 
        #no flip as it is right now (left child vs left child and right vs right)
        #OR the flipped version (left vs right and right vs left). We are searching
        #for only one true that will propogate up and make the entire or statement
        #true, a return False will stop that current call but if one path keeps
        #missing the false checks it will return true and that will go up. 


        
        if not root1 or not root2: return not root1 and not root2
        #Note, this simplifies if not r1 and not r2: return true 
                              #if not r1 or not r2: return false
        if root1.val!=root2.val: return False 
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

#The return ... or ... statement ensures that the method returns True if any valid configuration (either direct or flipped) is found at any level of the recursion.
#The True result propagates back up the recursive calls once the base cases are satisfied at the deepest level of the trees.

#Think: If one of them doesn't return false, the recursion will continue for that 
#branch, if none of the falses hit and it reaches the leaf nodes then it will return true and the true will propagate back up and eventually make the entire return true
