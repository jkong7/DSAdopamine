# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(nums): 
            if not nums: 
                return 
            max_value = max(nums)
            max_index = nums.index(max_value)
            leftnums=nums[:max_index]
            rightnums=nums[max_index+1:]
            return TreeNode(val=max_value, left=dfs(leftnums), right=dfs(rightnums))
        return dfs(nums)