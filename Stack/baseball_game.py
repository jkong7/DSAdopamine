class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        for op in operations: 
            if op not in ['+', 'D', 'C']: 
                stack.append(int(op))
            elif op=='+': 
                stack.append(stack[-1]+stack[-2])
            elif op=='C': 
                stack.pop()
            elif op=='D': 
                stack.append(2*stack[-1])
        return sum(stack)