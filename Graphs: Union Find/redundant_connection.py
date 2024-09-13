class UnionFind(): 
    def __init__(self, size): 
        self.parent=[i for i in range(size+1)]
        self.rank=[1]*(size+1)
    def find(self, x): 
        if self.parent[x]!=x: 
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self, x,y): 
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
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #One connected component 
        #Okay we go through and merge but if the two nodes already have the same parent
        #that means they were already connected and so we don't need to do it again, 
        #which means its redundant 
        n=len(edges)
        uf=UnionFind(n)

        for edge in edges: 
            if uf.find(edge[0])==uf.find(edge[1]): 
                return edge 
            else: 
                uf.union(edge[0], edge[1])