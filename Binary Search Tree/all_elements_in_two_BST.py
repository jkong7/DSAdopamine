# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """

        def inorder(node, result): 
            if not node: 
                return 
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)
        result1,result2=[],[]
        inorder(root1, result1)
        inorder(root2, result2)

        result=[]
        one, two=0,0
        while one<len(result1) and two<len(result2): 
            if result1[one]<=result2[two]: 
                result.append(result1[one])
                one+=1 
            else: 
                result.append(result2[two])
                two+=1 
        if one==len(result1): 
            while two<len(result2): 
                result.append(result2[two])
                two+=1 
        elif two==len(result2): 
            while one<len(result1): 
                result.append(result1[one])
                one+=1 
        return result 

