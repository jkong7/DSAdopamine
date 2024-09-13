# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        current=head
        length=0 
        while current: 
            length+=1 
            current=current.next 


        result=[0]*length 
        stack=[]
        current=head 
        index=-1 
        while current: 
            index+=1
            while stack and current.val>stack[-1][0]: #value, index 
                value, indexx=stack.pop()
                result[indexx]=current.val
            stack.append((current.val, index))
            current=current.next
        return result 
        


        