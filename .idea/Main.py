import pandas as pd
import collections
import re
from Graph import *

import networkx as nx


global ourGraph
global numOfNodes

def load_graph(path):
   file = pd.read_csv(path)
   numOfEdges=0  #for evaluation!!!
   df = pd.DataFrame(file, columns=None)
   graph1=graph()
   listOfNodes=[]
   i=-1
   while (i<len(df)):
        if i==-1:
               line = df.axes[1]._data
               source=line[0]
               dest=line[1]
               source=int(source)
               dest=int (dest)
               node1=node(source)
               node1.addNeighbor(dest)
               #numOfEdges=numOfEdges+1 #for evaluation!!!
               listOfNodes.append(source)
               listOfNodes.append(dest)
               graph1.nodes[source] = node1


        else:
            line=df.values[i]
            #in case its first time that source node apper
            if ( int(line[0]) not in graph1.getNodes()):
                node1=node(str(line[0]))
                node1.addNeighbor(line[1])
                #numOfEdges = numOfEdges + 1  #for evaluation!!!
                graph1.nodes[line[0]]=node1
            #in case node exist , add new neighbor
            else:
                graph1.nodes[line[0]].addNeighbor(line[1])
                #numOfEdges = numOfEdges + 1  #for evaluation!!!

            #check if source in listOfNodes, if not -add
            if (line[0] not in listOfNodes):
                listOfNodes.append(line[0])
            # check if dest in listOfNodes, if not -add
            if(line[1] not in listOfNodes):
                listOfNodes.append(line[1])

        i=i+1
   globals()['ourGraph']=graph1
   ourGraph.numOfNodes=len(listOfNodes)
   #print ("num of nodes: ")
   #print (ourGraph.numOfNodes)  # for evaluation!!!
   #print ("num Of edges: ")
   #print(numOfEdges)  #for evaluation!!!



def main():
    load_graph("C:\\Users\\Sahar Ben Baruch\\Desktop\\Wikipedia_votes.csv")
   # load_graph("C:\\Users\\Sahar Ben Baruch\Desktop\\anybeatAnonymized\\anybeatAnonymized\\anybeatAnonymized.csv")
    ourGraph.calculate_page_rank (0.85, 0.001, 20)
    print (ourGraph.get_top_nodes(10))

if __name__ == "__main__":
    main()