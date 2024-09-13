class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        from collections import Counter
        count=Counter(queryIP)
        four=(count['.']==3 and ':' not in count) if '.' in count else False 
        six=(count[':']==7 and '.' not in count) if ':' in count else False 

        if four: 
            parts=queryIP.split('.')
            for part in parts: 
                for char in part: 
                    if char.isalpha(): 
                        four=False
                if part=='': 
                    four=False
                if four: 
                    if int(part)<0 or int(part)>255 or (len(part)!=1 and part[0]=='0'):
                        four=False 
        if six: 
            parts=queryIP.split(':')
            for part in parts: 
                for char in part: 
                    if char.isalpha(): 
                        lower=char.lower()
                        if lower>'f':
                            six=False 
                if len(part)<1 or len(part)>4:
                    six=False
        if not four and not six: 
            return 'Neither'
        if four: 
            return 'IPv4'
        if six: 
            return 'IPv6'
