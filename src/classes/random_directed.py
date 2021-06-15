import networkx as nx
from random import randint

class RandomDirected(nx.Graph):
    def __init__( self, undirected_graph ):
        self.undirected_graph = undirected_graph

    def make_random_direction( self, edge ):
        if randint(1, 2) == 1:
            return [edge[0], edge[1]]
        else:
            return [edge[1], edge[0]]

    def direct_graph( self ):
        directed_graph = nx.DiGraph()
        for base_node in self.undirected_graph:
            directed_graph.add_node(base_node)
        for edge in self.undirected_graph.edges:
            arrow_nodes = self.make_random_direction( edge )
            directed_graph.add_edge( arrow_nodes[0], arrow_nodes[1] )
        self.directed_graph = directed_graph

    def find_descendent_edges( self, edge ):
        descendents = []
        for node in list(self.directed_graph.successors(edge[1])):
            descendents.append((edge[1], node))
        return descendents

    def make_descendent_info( self ):
        descendent_info = {}
        for edge in self.directed_graph.edges:
            descendent_info[edge] = self.find_all_descendent_edges( edge )
        self.descendent_info = descendent_info
        return descendent_info

    def find_all_descendent_edges( self, edge ):
        edge_queue = [edge]
        ret = [edge]
        while len(edge_queue) > 0:
            next_list = self.find_descendent_edges( edge_queue[0] )
            if len(next_list) > 0:
                for new_edge in next_list:
                    if new_edge not in ret:
                        edge_queue.append( new_edge )
                        ret.append( new_edge )
            del edge_queue[0]
        return ret
