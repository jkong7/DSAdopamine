# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=head 
        length=0 
        while current: 
            length+=1 
            current=current.next
        result=[-1]*length 
        stack=[]

        index=-1
        current=head 
        while current:
            index+=1 
            while stack and current.val>stack[-1][1]: 
                i, val=stack.pop()
                result[i]=index 
            stack.append((index, current.val))
            current=current.next

        dummy=ListNode(next=head)
        prev,current=dummy,head

        index=-1
        while current: 
            index+=1 
            if result[index]!=-1: 
                prev.next=current.next
            else: 
                prev=current
            current=current.next
        return dummy.next

        #next greater, next greater, next greater, powerful tool
        #But anyways yeah, three passes, one for length, one for making next greater
        #array, and one to act on next greater array by deleting nodes using prev
        #and current pointers (and head can be deleted so use dummy node)

        #Very smart way to do this with O(1) space 
        #First reverse the linked list, then if next_node in that reversed order 
        #is less than current, delete that, the undeleted nodes will inherently 
        #accumulate to the greatest seen node so far so it will always work 
        #Then reverse the modified list at the end too 

        prev,current=None, head 
        while current: 
            next_node=current.next
            current.next=prev 
            prev=current 
            current=next_node 

        fcurrent=prev 

        nextt=prev.next
        while nextt: 
            if nextt.val<prev.val: 
                prev.next=nextt.next
                nextt=nextt.next
            else: 
                prev=nextt
                nextt=nextt.next

        fprev=None
        while fcurrent: 
            next_node=fcurrent.next
            fcurrent.next=fprev
            fprev=fcurrent
            fcurrent=next_node
        return fprev 

        #The core principles still lies in the mono stack
        #O(1) space solution 
        #Just for review, reversing makes the head of the reversed list ALWAYS 
        #equal to the prev pointer, super important, and its always while current

