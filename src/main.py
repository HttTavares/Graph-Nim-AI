from classes.random_directed import RandomDirected
import networkx as nx

undirected_graph = nx.Graph()
nx.add_path( undirected_graph, [1,2,3,4,5,6,7])

def START_GAME( interger_list ):
    player = 0
    undirected_graph = nx.grid_graph( dim = interger_list )
    random_directed_graph = RandomDirected( undirected_graph )
    random_directed_graph.direct_graph()
    random_directed_graph.make_descendent_info()
    # r1 = Rule1(random_directed_graph)
    print(random_directed_graph.directed_graph.edges)
    print(random_directed_graph.descendent_info)
    print(player)

START_GAME( [10] )
