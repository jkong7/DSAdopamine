class UnionFind(): 
    def __init__(self, size): 
        self.parent=[i for i in range(size)]
        self.rank=[1]*size

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
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        #Count how many redundant connections there are? And then count how many are 
        #unconnected? 
        if len(connections)<n-1: 
            return -1 
        uf=UnionFind(n)
        for edge in connections: 
            uf.union(edge[0], edge[1])
        unique_components=len(set(uf.find(i) for i in range(n)))
        return unique_components-1 

