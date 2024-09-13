# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        number=[]
        current=head 
        while current: 
            number.append(str(current.val))
            current=current.next
        double=str(int(''.join(number))*2)

        index=0 
        current=head 
        while index<len(double): 
            if not current.next and index!=len(double)-1: 
                current.next=ListNode(int(double[index]))
            current.val=int(double[index])
            index+=1 
            current=current.next
        return head 

