  import networkx as nx
  from itertools import permutations
  from itertools import combinations
  from collections import defaultdict

#####
#1.a
  def generate_connected_subgraphs_n(n):
      all_nodes = range(1,n+1)
      min_edges_num = n-1
      max_edges_num = n * (n - 1)
      all_possible_edges = list(permutations(all_nodes, 2)) #generate all pairs of (v1,v2)
      print("all possible edges in the plot:",all_possible_edges) #print all edges

      all_graphs = [] #an empty list to keep all the graphs result
      # create all combinations of number of edges (n-1, n^2)
      j = 0 #graphs counter
      for num in range(min_edges_num, max_edges_num+1): #for every possible number of edges (graph size)
        edges_combs = list(permutations(all_possible_edges, num)) #get all combinations of "num" edges
        for i in edges_combs: #for each combination of nodes, generate a new graph that  includes all nodes and this combination's edges
          graph_temp = nx.DiGraph()
          graph_temp.add_nodes_from(range(1, n+1))
          graph_temp.add_edges_from(i)
          if(nx.is_connected(graph_temp.to_undirected())): #check if the graph is directed
            is_isomorphic = False
            for chosen_graph in all_graphs:
              is_isomorphic = nx.is_isomorphic(graph_temp, chosen_graph)
              if(is_isomorphic):
                break;
            if(is_isomorphic == False ): #if the graph is unique
              all_graphs.append(graph_temp)
      return all_graphs


  for n in range(1,4):
    print("____________________________________________________________________")
    x = generate_connected_subgraphs_n(n)
    print("for n = ",n,"number of subgraphs is:",len(x))
    num = 1
    for i in x:
      print("graph number",num,i.edges)
      num = num+1



#######
#1. b- print the results of the program for n = 1-4

for n in range(1,5):
  generate_connected_subgraphs_n(n)
