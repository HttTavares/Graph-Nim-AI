from classes.random_directed import RandomDirected
from Rules.rule1 import Rule1
import networkx as nx

undirected_graph = nx.Graph()
nx.add_path( undirected_graph, [1,2,3,4,5,6,7])

def START_GAME( interger_list ):
    player = 0
    undirected_graph = nx.grid_graph( dim = interger_list )
    random_directed_graph = RandomDirected( undirected_graph )
    random_directed_graph.direct_graph()
    random_directed_graph.make_descendent_info()
    r1 = Rule1( random_directed_graph )
    print(list(random_directed_graph.directed_graph.edges))
    # print( list(random_directed_graph.directed_graph.edges)[0] )
    edge1 = list(random_directed_graph.directed_graph.edges)[0]
    r1.destroy_directed_edge( (edge1[0], edge1[1]) )
    print(list(random_directed_graph.directed_graph.edges))
    player = 1 - player
    r1.calculate_victory( player )

    edge1 = list(random_directed_graph.directed_graph.edges)[0]
    r1.destroy_directed_edge( (edge1[0], edge1[1]) )
    print(list(random_directed_graph.directed_graph.edges))
    player = 1 - player
    r1.calculate_victory( player )

    edge1 = list(random_directed_graph.directed_graph.edges)[0]
    r1.destroy_directed_edge( (edge1[0], edge1[1]) )
    print(list(random_directed_graph.directed_graph.edges))
    player = 1 - player
    r1.calculate_victory( player )

    edge1 = list(random_directed_graph.directed_graph.edges)[0]
    r1.destroy_directed_edge( (edge1[0], edge1[1]) )
    print(list(random_directed_graph.directed_graph.edges))
    player = 1 - player
    r1.calculate_victory( player )



START_GAME( [10] )
