interface TRIP_PLANNER:

    # Returns the positions of all the points-of-interest that belong to
    # the given category.
    def locate_all(
            self,
            dst_cat:  Cat?           # point-of-interest category
        )   ->        ListC[RawPos?] # positions of the POIs

    # Returns the shortest route, if any, from the given source position
    # to the point-of-interest with the given name.
    def plan_route(
            self,
            src_lat:  Lat?,          # starting latitude
            src_lon:  Lon?,          # starting longitude
            dst_name: Name?          # name of goal
        )   ->        ListC[RawPos?] # path to goal

    # Finds no more than `n` points-of-interest of the given category
    # nearest to the source position.
    def find_nearby(
            self,
            src_lat:  Lat?,          # starting latitude
            src_lon:  Lon?,          # starting longitude
            dst_cat:  Cat?,          # point-of-interest category
            n:        nat?           # maximum number of results
        )   ->        ListC[RawPOI?] # list of nearby POIs


# helper function for building unique_positions list          
def in_list(list, element): 
    let curr=list 
    while curr: 
        if curr.data==element: 
            return True 
        curr=curr.next
    return False 
    
    
class TripPlanner (TRIP_PLANNER):
    let road_segments 
    let pois
    let poi_table
    let unique_positions
    let pos_to_vertex
    let vertex_to_pos
    let graph 
    
    def __init__(self, roads, pois): 
        self.road_segments = roads #stores input road segments vectors 
        self.pois = pois #stores input POI vectors 
        self.poi_table=HashTable(100,make_sbox_hash())
        self.unique_positions = None
        self.pos_to_vertex = HashTable(len(self.pois), make_sbox_hash())
        self.vertex_to_pos = HashTable(len(self.pois), make_sbox_hash())
        #graph initialized later with the length of the unique_positions linked list 
        
        #Note to self: roads and pois are the inputs to class initialization
        #every other instance variable is to support the functionality 
        #provided by the class methods 
        
        #initializes poi_table hashtable 
        for poi in pois: 
            let lat=poi[0]
            let lon = poi[1]
            let category=poi[2]
            let pois=poi[3]
            let position=[lat, lon]
            if not self.poi_table.mem?(category):
                self.poi_table.put(category, cons(position, None))
            else: 
                let new_list=self.poi_table.get(category)
                new_list=cons(position, new_list)
                self.poi_table.put(category, new_list)
                
       
        #initializes unique_positions list        
        for road in self.road_segments:
            if not in_list(self.unique_positions, [road[0], road[1]]):
                self.unique_positions = cons([road[0], road[1]], self.unique_positions)
            if not in_list(self.unique_positions, [road[2], road[3]]):
                self.unique_positions = cons([road[2], road[3]], self.unique_positions)
                                   
        #initializes bidirectional mapping (pos_to_vertex and vertex_to_pos) and graph 
        self.initialize_graph()
        
        #//end of init method   
        
        
        
    #creates bidirectional mapping between pos and vertexes as well as the graph     
    def initialize_graph(self): 
        let current = 0
        let curr = self.unique_positions
        
        while curr:
            self.pos_to_vertex.put(curr.data, current)
            self.vertex_to_pos.put(current, curr.data)
            curr = curr.next
            current = current + 1
        #initializes graph with the number of vertices as the current value (number of unique positions)
        self.graph = WUGraph(current)
        #sets vertices and weights in graph 
        for road in self.road_segments:
            self.graph.set_edge(self.pos_to_vertex.get([road[0], road[1]]),
                                self.pos_to_vertex.get([road[2], road[3]]),
                                ((road[2]-road[0])**2+(road[3]-road[1])**2)**0.5)   
                    
                                
    def get_all_pois_by_position_and_category(self, position, category):
        let result=None
        for poi in self.pois: 
            if poi[0]==position[0] and poi[1]==position[1] and poi[2]==category: 
                result=cons(poi, result)
        return result 
                
                                
    #djikstra's algorithm function that returns the shortest distances between a source vertex 
    #and all other vertices in the graph as well as the predecessors for each vertex in the graph 
    #created using the shortest distances                              
    def djikstra(self, src_vertex):
        let dist=[inf for _ in range(self.graph.n_vertices())]
        let pred=[None for _ in range(self.graph.n_vertices())]
        let done=[False for _ in range(self.graph.n_vertices())]
        dist[src_vertex]=0 
        let pq=BinHeap(self.graph.n_vertices(),  λ x, y: dist[x] < dist[y])
        pq.insert(src_vertex)
        while pq.len() != 0: 
            let min_vertex=pq.find_min()
            pq.remove_min()
            if not done[min_vertex]: 
                done[min_vertex]=True 
                let curr = self.graph.get_adjacent(min_vertex)
                while curr:
                    let edge_weight=self.graph.get_edge(min_vertex, curr.data)
                    if edge_weight is None: 
                        pass
                    if dist[min_vertex] + edge_weight < dist[curr.data]: 
                        dist[curr.data]=dist[min_vertex] + edge_weight
                        pred[curr.data]=min_vertex
                        pq.insert(curr.data)
                    curr = curr.next
        return [dist, pred] 

                 
           
    def locate_all(self, dst_cat): 
        if self.poi_table.mem?(dst_cat): 
		        return self.poi_table.get(dst_cat) 
        else: 
            return None
            
            
            
    def plan_route(self, src_lat, src_lon, dst_name): 
        let src_vertex=self.pos_to_vertex.get([src_lat, src_lon])
        let dst_vertex = None
        for poi in self.pois: 
            if poi[3]==dst_name: 
                dst_vertex=self.pos_to_vertex.get([poi[0], poi[1]])
        if dst_vertex is None: 
            return None
        let result=self.djikstra(src_vertex)
        let pred=result[1]
        let dist=result[0]
        let list=cons(self.vertex_to_pos.get(dst_vertex), None)
        if dist[dst_vertex]==inf: 
            return None
        else: 
            let curr=pred[dst_vertex]
            while curr is not None: 
                list=cons(self.vertex_to_pos.get(curr),list)
                curr = pred[curr]
        return list 
        
        


    def find_nearby(self, src_lat, src_lon, dst_cat, n):
        let src_vertex = self.pos_to_vertex.get([src_lat, src_lon])
        let result_dijkstra = self.djikstra(src_vertex)
        let dist = result_dijkstra[0]

        
        let pq = BinHeap(self.graph.n_vertices(), lambda x, y: (dist[x] < dist[y]))
        
        # Insert vertex indices into the priority queue
        for i in range(len(dist)): 
            pq.insert(i)
        
        let count = 0  
        let result = None     
        while pq.len() != 0 and count < n: 
            let vertex = pq.find_min()
            pq.remove_min()
            let pos = self.vertex_to_pos.get(vertex)
            let pois = self.get_all_pois_by_position_and_category(pos, dst_cat)
            while pois is not None:
                result = cons(pois.data, result)
                pois = pois.next
                count =count+ 1
                if count >= n: 
                    break 
        return result