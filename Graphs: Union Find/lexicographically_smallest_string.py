class UnionFind(): 
    def __init__(self):
        self.parent=[i for i in range(26)]
        self.rank=[1]*26 
        self.minn=[i for i in range(26)]


    def find(self, x): 
        if self.parent[x]!=x: 
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y): 
        rootx=self.find(x)
        rooty=self.find(y) 

        if rootx!=rooty:
            if self.rank[rootx]>self.rank[rooty]: 
                self.parent[rooty]=rootx
                self.minn[rootx]=min(self.minn[rootx], self.minn[rooty])
            elif self.rank[rootx]<self.rank[rooty]: 
                self.parent[rootx]=rooty
                self.minn[rooty]=min(self.minn[rooty], self.minn[rootx])
            else: 
                self.parent[rooty]=rootx
                self.minn[rootx]=min(self.minn[rootx], self.minn[rooty])
                self.rank[rootx]+=1 

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        def key(x): 
            return ord(x)-ord('a')
        n=len(s1)
        uf=UnionFind()
        for i in range(n): 
            uf.union(key(s1[i]), key(s2[i]))
        result=[]
        for i in range(len(baseStr)): 
            result.append(chr(uf.minn[uf.find(key(baseStr[i]))]+97))
        return ''.join(result)

