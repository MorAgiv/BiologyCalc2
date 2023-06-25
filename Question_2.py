# 2
import itertools
import networkx as nx
from itertools import permutations
from itertools import combinations
from collections import defaultdict


def generate_subgraphs_of_g(g_input,n):
    all_nodes = g_input.nodes()
    min_edges_num = min(n-1, g_input.number_of_edges())
    max_edges_num = len(g_input.edges())
    all_possible_edges = g_input.edges()
    print("all possible edges in the plot:")
    for i in all_possible_edges:
      print(i)
    all_graphs = []
    # create all combinations of number of edges (n-1, n^2)
    j = 0
    for num in range(min_edges_num, max_edges_num+1): #for every possible number of edges
      edges_combs = list(permutations(all_possible_edges, num)) #get all combinations of "num" edges
      for i in edges_combs: #for each combination of nodes, generate a new graph
         graph_temp = nx.DiGraph()
         graph_temp.add_nodes_from(range(1, n+1))
         graph_temp.add_edges_from(i)
         if(nx.is_connected(graph_temp.to_undirected())):
          is_isomorphic = False
          for chosen_graph in all_graphs:
            is_isomorphic = nx.is_isomorphic(graph_temp, chosen_graph)
            if(is_isomorphic):
              break;
          if(is_isomorphic == False ): #if the graph is unique
            all_graphs.append(graph_temp)
            j = j+1
            print("graph number",num,graph_temp.edges)
    return all_graphs

#test
n = 3
g = nx.DiGraph()
g.add_nodes_from(range(1, n+1)) # Add nodes
g.add_edge(1,2)

g.add_edge(3,2)
g.add_edge(2,3)
