class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        colored=0 
        result=[0]*len(queries) 
        indexht={}
        colorht={}

        #ht    index: color 
        #ht    color: count 
        for i,q in enumerate(queries): 
            index, color=q[0], q[1]
            if index not in indexht: 
                indexht[index]=color 
                if color not in colorht: 
                    colored+=1 
                    colorht[color]=1
                else: 
                    colorht[color]+=1 
            elif index in indexht: 
                if indexht[index]!=color: 
                    colorht[indexht[index]]-=1
                    if colorht[indexht[index]]==0: 
                        del colorht[indexht[index]]
                        colored-=1 
                    if color not in colorht: 
                        colored+=1 
                        colorht[color]=1 
                    else: 
                        colorht[color]+=1 
                    indexht[index]=color 
            result[i]=colored 
        return result 

        #But yeah, two hts, one thats index:color and another thats color: count, 
