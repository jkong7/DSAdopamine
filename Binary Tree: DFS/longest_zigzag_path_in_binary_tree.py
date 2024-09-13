# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result=0 
        def dfs(root, direction, depth): 
            if not root: 
                return 
            self.result=max(self.result, depth)
            if direction=='right': 
                dfs(root.right, 'left', depth+1)
                dfs(root.left, 'right', 1)
            if direction=='left': 
                dfs(root.left, 'right', depth+1)
                dfs(root.right, 'left', 1)
        dfs(root, 'right', 0)
        dfs(root, 'left', 0)
        return self.result

        #We pass in a direction to each recursive call to tell it which direction 
        #to go to next, if we zigzag we add 1 to current depth, if we reset 
        #which is go the OPPOSITE direction of the zigzag, we reset depth back to 1
        #and recurse from starting there 
        #The universal result variable will keep track of all possible depths and
        #update to the largest 