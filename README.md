# BiologyCalc2
by Revital Badalov and Mor Agiv

## About
this code solves the two problems we recieved for homework:
#### 1
a program that gets as input a positive integer 𝑛 and generates all connected sub-graphs of size
The algorithm:
First we calculate all the possible edges and nodes number using the n.
Then we create all the possible number of edges (n-1, n^2)
then, for every possible number of edges, we generate all edges combinations of that size and create a graph that contains them.
Then we check for each graph whether it's connected and unique (non-isomorphic to all the others) and if so, we keep it.



#### 2
a program that gets as input positive integer 𝑛 and a graph output all sub-graphs of size 𝑛 and count how
many instances appear of each motif.
The algorithm:
The only difference here is that we take all the possible edges and nodes from the given graph, and we calculate the min/max edges number using the given graph's edges.
First we create all the possible number of edges (n-1, n^2)
then, for every possible number of edges, we generate all edges combinations of that size and create a graph that contains them.
Then we check for each graph whether it's connected and unique (non-isomorphic to all the others) and if so, we keep it.
