# Membuat Logic untuk visualisasi Streamlit 
import networkx as nx
# Membuat Logic untuk visualisasi Streamlit 
import networkx as nx
class Graf:
    def __init__(self):
        self.graph = nx.Graph()
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph.add_node(vertex)
            return True
        return False
        
    def add_edge(self, v1, v2, w):
        if self.graph.has_node(v1) and self.graph.has_node(v2):
            self.graph.add_edge(v1, v2, weight=w)
        return False
    
    def get_graph(self):
        return self.graph
    
    def get_all_vertex(self):
        return self.graph.nodes()
    
    def get_all_edges(self):
        return self.graph.edges()
    
    def get_all_vertex_with_weight(self):
        return self.graph.edges(data='weight', default=1)
    
    def find_shortest_path(self, start, end):
        try:
            path = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
            cost = nx.shortest_path_length(self.graph, source=start, target=end, weight='weight')
            return path, cost
        except nx.NetworkXNoPath:
            return None, 0
        except nx.NodeNotFound:
            return None, 0

    @property
    def adj_list(self):
        return nx.to_dict_of_dicts(self.graph)
   
