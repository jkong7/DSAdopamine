from collections import defaultdict 
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #Same logic as just counting number of connected components (keep global
        #visited set). But now, we only increment self.result IF the number of 
        #nodes in the connected comp (comp nodes) produces number of edges 
        #that matches the expected number of edges
        #The theory is: expected numb of edges for k nodes in an undirected 
        #connected component is k*(k-1)//2
        #Actual: actual+=len(graph[node]) for node in component_nodes //2 (adj list
        #len for a key is numb of edges from that node)
        graph=defaultdict(list)
        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        seen=set()
        self.result=0 
        def graph_iterator(graph): 
            for i in range(n): 
                if i not in seen: 
                    comp_nodes=[]
                    dfs(comp_nodes, i)
                    if complete(comp_nodes): 
                        self.result+=1 
        def dfs(comp_nodes, start): 
            seen.add(start)
            comp_nodes.append(start)
            for neighbor in graph[start]: 
                if neighbor not in seen: 
                    dfs(comp_nodes, neighbor)
        def complete(comp_nodes): 
            k=len(comp_nodes)
            expected=k*(k-1)//2
            actual=0 
            for node in comp_nodes: 
                actual+=len(graph[node])
            actual=actual//2 
            return expected==actual 
        graph_iterator(graph)
        return self.result