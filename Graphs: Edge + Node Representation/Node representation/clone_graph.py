"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: 
            return None 
        old_to_new={}
        def dfs(node): 
            if node in old_to_new: 
                return old_to_new[node]
            copy=Node(node.val)
            old_to_new[node]=copy 
            for neighbor in node.neighbors: 
                if neighbor not in old_to_new: 
                    dfs(neighbor) #Will recursively clone ALL nodes (NO neighbors)
                old_to_new[node].neighbors.append(old_to_new[neighbor]) #Neighbors are only built AFTER all clone nodes have been built, this line makes the proper
                #connections 
        dfs(node)
        return old_to_new[node]
        
        
        #This solution layout makes it more clear that we are focusing on 
        #returning the copy of node (neetcodes solution): 
        old_to_new={}
        def dfs(node): 
            if node in old_to_new: 
                return old_to_new[node]
            copy=Node(node.val)
            old_to_new[node]=copy 
            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor))
            return copy 
        return dfs(node) if node else None
        

        #Create the adj list clone that will store cloned nodes (created new ones
        #using Node class) and its neighbors will be populated 
        #Return old_to_new[node]


