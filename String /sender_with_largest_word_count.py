class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """

        
        from collections import defaultdict 
        ht=defaultdict(int)
        maxx=0 
        name='a'
        for i, message in enumerate(messages): 
            space=0 
            for char in message: 
                if char==' ': 
                    space+=1 
            ht[senders[i]]+=space+1 
            if ht[senders[i]]>maxx: 
                maxx=ht[senders[i]]
                name=senders[i]
            elif ht[senders[i]]==maxx: 
                name=max(name, senders[i])
        return name 



