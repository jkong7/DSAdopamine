# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev=None 
        self.mindiff=float('inf')
        def inorder(root): 
            if not root:   #Base case, stop further recursion/function calls 
                return 
            inorder(root.left)
            if self.prev is not None: 
                if root.val-self.prev.val<self.mindiff:
                    self.mindiff=root.val-self.prev.val
            self.prev=root 
            inorder(root.right)
        inorder(root)
        return self.mindiff
        #Using instance variables for their mutability is the most concise/easiest

        # prev current difference checker using inorder BST traversal 
        #which goes ascending order (mindiff will always be a diff between two
        #adjacent values in this traversal so using prev current is the way to go)

        #Can also obv do with mutable DT inside function (array): 
        def inorder(root, prev, mindiff): 
            if not root: 
                return 
            inorder(root.left, prev, mindiff)
            if prev[0] is not None: 
                if root.val-prev[0].val<mindiff[0]: 
                    mindiff[0]=root.val-prev[0].val
            prev[0]=root 
            inorder(root.right, prev, mindiff)
        mindiff=[float('inf')]
        inorder(root, [None], mindiff)
        return mindiff[0]    

        #O(n) time O(h) space (recursion stack) O(1) EXTRA space for both 
        #(in place diff operation)        
