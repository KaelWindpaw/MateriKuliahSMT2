"""
Graph implementation untuk sistem prioritas posisi pembeli
Menghitung jarak terdekat dari pusat penjualan tiket
"""

import math
from typing import Dict, List, Tuple


class Node:
    def __init__(self, node_id, x, y, name=""):
        self.id = node_id
        self.x = x
        self.y = y
        self.name = name
        self.neighbors = []
    
    def __repr__(self):
        return f"Node({self.id}, {self.name})"


class Graph:
    """
    Implementasi Graph untuk merepresentasikan posisi pembeli
    dan menghitung prioritas berdasarkan jarak ke pusat penjualan
    """
    
    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.edges = []
        self.center = None  # Pusat penjualan tiket
    
    def add_node(self, node_id: int, x: float, y: float, name: str = ""):
        """Tambahkan node (posisi pembeli) ke graph"""
        if node_id not in self.nodes:
            node = Node(node_id, x, y, name)
            self.nodes[node_id] = node
            return True
        return False
    
    def set_center(self, node_id: int):
        """Set pusat penjualan tiket"""
        if node_id in self.nodes:
            self.center = self.nodes[node_id]
            return True
        return False
    
    def add_edge(self, node_id1: int, node_id2: int, weight: float = None):
        """Tambahkan edge (hubungan) antar node"""
        if node_id1 in self.nodes and node_id2 in self.nodes:
            if weight is None:
                weight = self.calculate_distance(node_id1, node_id2)
            
            self.edges.append((node_id1, node_id2, weight))
            self.nodes[node_id1].neighbors.append(node_id2)
            return True
        return False
    
    def calculate_distance(self, node_id1: int, node_id2: int) -> float:
        """Hitung jarak Euclidean antara dua node"""
        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            return 0
        
        node1 = self.nodes[node_id1]
        node2 = self.nodes[node_id2]
        
        distance = math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)
        return round(distance, 2)
    
    def get_distance_from_center(self, node_id: int) -> float:
        """Hitung jarak node dari pusat penjualan tiket"""
        if self.center is None or node_id not in self.nodes:
            return float('inf')
        
        return self.calculate_distance(self.center.id, node_id)
    
    def get_nearest_nodes(self, top_n: int = None) -> List[Tuple[int, str, float]]:
        """
        Dapatkan node terdekat dari pusat
        Return: List of (node_id, name, distance)
        """
        if self.center is None:
            return []
        
        distances = []
        for node_id, node in self.nodes.items():
            if node_id != self.center.id:
                distance = self.get_distance_from_center(node_id)
                distances.append((node_id, node.name, distance))
        
        # Sort berdasarkan jarak (terdekat dulu)
        distances.sort(key=lambda x: x[2])
        
        if top_n is not None:
            return distances[:top_n]
        
        return distances
    
    def get_priority_queue(self) -> List[Dict]:
        """
        Dapatkan antrian prioritas berdasarkan jarak dari pusat
        Return: List of dict dengan informasi prioritas
        """
        priority_list = []
        nearest_nodes = self.get_nearest_nodes()
        
        for idx, (node_id, name, distance) in enumerate(nearest_nodes, 1):
            priority_list.append({
                'priority': idx,
                'node_id': node_id,
                'name': name,
                'x': self.nodes[node_id].x,
                'y': self.nodes[node_id].y,
                'distance': distance
            })
        
        return priority_list
    
    def get_all_nodes_info(self) -> List[Dict]:
        """Dapatkan informasi semua node"""
        nodes_info = []
        for node_id, node in self.nodes.items():
            distance_from_center = self.get_distance_from_center(node_id) if self.center else "N/A"
            nodes_info.append({
                'id': node_id,
                'name': node.name,
                'x': node.x,
                'y': node.y,
                'distance_from_center': distance_from_center,
                'is_center': node_id == self.center.id if self.center else False
            })
        return nodes_info
    
    def get_graph_info(self) -> Dict:
        """Dapatkan informasi lengkap graph"""
        return {
            'total_nodes': len(self.nodes),
            'total_edges': len(self.edges),
            'center': self.center.name if self.center else None,
            'nodes': self.get_all_nodes_info()
        }
    
    def dijkstra(self, start_id: int) -> Dict:
        """
        Implementasi Dijkstra untuk menemukan rute terpendek
        """
        if start_id not in self.nodes:
            return {}
        
        distances = {node_id: float('inf') for node_id in self.nodes}
        distances[start_id] = 0
        unvisited = set(self.nodes.keys())
        
        while unvisited:
            current = min(unvisited, key=lambda x: distances[x])
            
            if distances[current] == float('inf'):
                break
            
            for neighbor in self.nodes[current].neighbors:
                if neighbor in unvisited:
                    edge_distance = self.calculate_distance(current, neighbor)
                    new_distance = distances[current] + edge_distance
                    
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
            
            unvisited.remove(current)
        
        return distances
