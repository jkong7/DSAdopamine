class WUGraph (WUGRAPH):
    let size 
    let adj_matrix  
    
    def __init__(self, size: nat?): 
        self.size=size
        self.adj_matrix=[[None for _ in range(size)] for _ in range(size)]
        
    def n_vertices(self): 
        return self.size
        
    def get_edge(self, u, v):
        return self.adj_matrix[u][v]
        
    def set_edge(self, u, v, w): 
        self.adj_matrix[u][v]=w
        self.adj_matrix[v][u]=w
        
    def get_adjacent(self, v): 
        let list = None
        for u in range(self.size): 
            if self.adj_matrix[v][u] is not None: 
                list=cons(u, list)
        return list 
        
    def get_all_edges(self):
        let list = None
        for u in range(self.size):
            for v in range(u, self.size):
                  if self.adj_matrix[u][v] is not None: 
                      list = cons(WEdge(u, v, self.adj_matrix[u][v]), list)                      
        return list