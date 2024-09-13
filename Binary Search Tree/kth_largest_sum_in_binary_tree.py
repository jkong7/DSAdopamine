# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        #Size k heap + level order traversal 
        #pop whenever size of heap exceeds k 
        #minheap with pos values 
        import heapq
        from collections import deque 
        q=deque([root])
        heap=[]
        while q: 
            flag=False
            levelsum=0 
            for _ in range(len(q)): 
                current=q.popleft()
                if current: 
                    flag=True
                    levelsum+=current.val 
                    if current.left: q.append(current.left)
                    if current.right: q.append(current.right)
            if flag: 
                heapq.heappush(heap, levelsum)
                if len(heap)>k: 
                    heapq.heappop(heap)
        return -1 if len(heap)<k else heap[0]
        #for kth LARGEST, size k heap and pop whenever exceeds k
        #and put in POSITIVE values to the MINHEAP
        #If it was kth smallest, append -levelsum vals, same popping, but then return
        #-heap[0] 
