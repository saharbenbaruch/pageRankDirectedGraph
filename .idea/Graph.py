from __future__ import division
import collections
import operator

class node:
    def __init__(self,name):
        self.name=name
        self.pageRank=0
        self.dest=[]

    def addNeighbor(self,neighbor):
       self.dest.append(neighbor)

    def get_pageRank(self):
        return self.pageRank




class graph:
    def __init__(self):
        self.nodes={}
        numOfNodes=0


    def getNodes(self):
        return self.nodes

    def calculate_page_rank(self,b=0.85, j=0.001, maxIterations=20):
        # init
        curIteration = 0
        i=0
        while(i<len(self.nodes)) :
           self.nodes.values()[i].pageRank= float(1) / self.numOfNodes
           i=i+1
        #start new iteration
        while (curIteration < maxIterations):
            delta=0;
            s =0
            curIteration = curIteration + 1
            calulationTable = {}
            for curNode in self.nodes.values():
                for neighbor in curNode.dest:
                    if (calulationTable.get(neighbor)!=None):
                        calulationTable[neighbor]= calulationTable[neighbor] +b*(curNode.get_pageRank()/len(curNode.dest))
                    # if neighbor isnt exist in calulationTable- need to add it.
                    else:
                        calulationTable[neighbor]=b*(curNode.get_pageRank()/len(curNode.dest))

            for node in calulationTable:
                s=s+calulationTable[node];
            #need to insert to each Node part of s. (when b<1) & new page rank according CalculationTalbe.
            extraPerNode= (1-s)/self.numOfNodes
            for node in self.nodes.values():
                prvPageRank = node.get_pageRank()
                if (calulationTable.has_key(int(node.name))):
                    node.pageRank=calulationTable[int(node.name)]+extraPerNode
                else:
                    node.pageRank = extraPerNode
                delta=delta+abs(prvPageRank-node.get_pageRank())
           #in case delta smaller than given epsilon
            if (delta<j):
                break


    #Returns the PageRank of a specific node.
    def get_PageRank(self,node_name):
        node1=self.nodes.get(int(node_name))
        if (node1 != None):
            return node1.get_pageRank()
        else:
            return -1



    #Returns a list of n nodes with the highest PageRank.
    def get_top_nodes(self,n):
        if n>0 & n<len(self.nodes):
            list=self.get_all_PageRank();
            nList=list[0:n]
            return nList

        else:
            print (" n is bigger then num of nodes or smaller then 0.")


    #return <node name, Page Rank>
    def get_all_PageRank(self):
        list={}
        items= self.nodes.items()
        i=0
        while (i<len(self.nodes)):
            tempNode=items[i]
            list[str(tempNode[0])]=tempNode[1].get_pageRank()
            i=i+1

        sortedList=sorted(list.items(), key=operator.itemgetter(1),reverse=1)
        return sortedList


    def isExist(self,node):
        i=0;
        while i<len(node):
            if (node[i]==node):
                return 1;
            else:
                i=i+1

