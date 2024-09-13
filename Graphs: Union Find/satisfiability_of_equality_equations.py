class UnionFind(): 
    def __init__(self):
        self.parent=[i for i in range(26)]
        self.rank=[1]*26 
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
            elif self.rank[rootx]<self.rank[rooty]: 
                self.parent[rootx]=rooty
            else: 
                self.parent[rooty]=rootx
                self.rank[rootx]+=1 

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        #Union together ==
        #Then go through the !=, if parent of those two are the same, then return false 
        #
        def key(x): 
            return ord(x)-ord('a')
        uf=UnionFind()
        for equation in equations: 
            if '==' in equation: 
                uf.union(key(equation[0]), key(equation[3])) 
        for equation in equations: 
            if '!=' in equation: 
                if uf.find(key(equation[0]))==uf.find(key(equation[3])): 
                    return False 
        return True 
