class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for char in s:
            if char == ')':
                rightnum = ''
                while stack and stack[-1] != '(':
                    rightnum = stack.pop() + rightnum
                stack.pop()  # To get rid of '('

                # Now evaluate the expression inside the parentheses
                rightnum = rightnum.replace('-', '+-')
                rightnum = rightnum.split('+')
                # Ensure no empty strings are included in the summation
                result = sum(int(num) for num in rightnum if num)
                stack.append(str(result))
            else:
                stack.append(char)

        # Now there are no more parentheses, just a string expression like '2-1+2'
        # Apply the same code used to evaluate between-paren-expression to evaluate final result
        expression = ''.join(stack).replace('-', '+-')
        numbers = expression.split('+')
        return sum(int(num) for num in numbers if num)