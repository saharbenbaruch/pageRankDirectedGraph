This API implements Page Rank algorithm for directed unweighted graph.
Our API expect getting .csv file contain <source id , destination id> without headers.

We created class Node - contains 'name' , 'pageRank' , 'dest' (represent all nodes 
that current node has edges to them.)

we created class for Graph- contains 'numOfNodes' and dictionary of 'Nodes'

Instructions:

load_graph(path) for read the dataset and creating graph out of it.
This function collects all new nodes its occur and add them to list of all nodes so we could
know how many unique nodes the graph contains.

The function breaks every line to source and destination nodes and create objects of them.
We use 'addNeighbor(Node)'  to add destination node to source node.

we add all nodes to graph .
The graph is global variable .

calculate_page_rank (beta, epsilon, maxIteration) - generate by graph object.
Its run over all nodes from nodes dictionary and use different dictionary calls 'calculateTable'
to save the sum contribution of current node (in act of source) in page rank of destination node.
we calculate (1-s)/ numOfNodes and give that to each node in the end of each iteration.


for example, node A has edge to node B.
A' rank is 5  -> B will get 1/5 * a'rank * beta + (1-s)/numOfNodes

we check that total epsilon is lower than given epsilon, else - break.
