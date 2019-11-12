import pandas as pd
import collections
import re
from Graph import *

global ourGraph
global numOfNodes

def load_graph(path):
   file = pd.read_csv(path)
   df = pd.DataFrame(file, columns=None)
   graph1=graph()
   listOfNodes=[]
   i=-1
   while (i<len(df)):
        if i==-1:
           line = df.axes[1]._data

        else:
            line=df.values[i]
        #in case its first time that source node apper
        if (line[0] not in graph1.getNodes()):
            node1=node(str(line[0]))
            node1.addNeighbor(line[1])
            #node1.pageRank=i  // just for test.
            graph1.nodes[line[0]]=node1
        #in case node exist , add new neighbor
        else:
            graph1.nodes[line[0]].addNeighbor(line[1])

        #check if source in listOfNodes, if not -add
        if (line[0] not in listOfNodes):
            listOfNodes.append(line[0])
        # check if dest in listOfNodes, if not -add
        if(line[1] not in listOfNodes):
            listOfNodes.append(line[1])

        i=i+1
   globals()['ourGraph']=graph1
   globals() ['numOfNodes']=len(listOfNodes)
   #print (globals() ['numOfNodes'])



def main():
    load_graph("C:\\Users\\Sahar Ben Baruch\\Desktop\\test.csv")
 #   list=ourGraph.get_all_PageRank()
 #   print (list)
    sortedList=ourGraph.get_top_nodes(2)
#    rank=ourGraph.get_PageRank("15")
    print (sortedList)


if __name__ == "__main__":
    main()