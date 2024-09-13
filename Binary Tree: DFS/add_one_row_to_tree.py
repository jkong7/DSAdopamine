# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """

        def dfs(node, val, depth, currentdepth): 
            if not node: 
                return 
            currentdepth+=1 
            if currentdepth==depth-1: 
                left=node.left
                node.left=TreeNode(val=val, left=left)
                right=node.right 
                node.right=TreeNode(val=val, right=right)
            dfs(node.left, val, depth, currentdepth)
            dfs(node.right, val, depth, currentdepth)
        if depth==1: 
            newroot=TreeNode(val=val, left=root)
            return newroot
        dfs(root, val, depth, 0)
        return root 
        #thought dfs would have been more intuitive so I switched to 
        #that. Algo is: Whenever your node is at depth-1, make a sandwich link 
        #between depth-1 -> new -> depth. And then the edge case of depth==1 you 
        #just make a new node with its left subtree as the old whole tree


        #Did BFS/level order traversal too! BFS is much faster and that should make
        #sense, every node that needs to be processed is on the same level so the 
        #moment we get to that level, we do it all at once and then break out and 
        #return 
        from collections import deque 
        q=deque([root])
        level=0 
        firstflag=False
        if depth==1: 
            newroot=TreeNode(val=val, left=root)
            return newroot

        while q: 
            level+=1 
            if level==depth-1: #We want to link everything on this level to new vals
                firstflag=True
            for _ in range(len(q)): 
                current=q.popleft()
                if firstflag: 
                    left=current.left
                    current.left=TreeNode(val=val, left=left)
                    right=current.right 
                    current.right=TreeNode(val=val, right=right)
                if current.left: 
                    q.append(current.left)
                if current.right: 
                    q.append(current.right)
            if firstflag: 
                break 
        return root 
                

