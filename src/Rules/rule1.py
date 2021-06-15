import networkx as nx

class Rule1():

    def __init__(self, random_directed_graph ):
        self.random_directed_graph = random_directed_graph

    def make_edge( self, input1, input2 ):
        return (int(input1), int(input2))

    def destroy_directed_edge( self, edge ):
        for removing_edge in self.random_directed_graph.find_all_descendent_edges( edge ):
            self.random_directed_graph.directed_graph.remove_edge(removing_edge[0], removing_edge[1])

    def calculate_victory( self, player ):
        for edge in self.random_directed_graph.directed_graph.edges:
            if len(self.random_directed_graph.descendent_info[ edge ]) > 1:
                return False
            else:
                print("player: " + str(player) + " won!")
