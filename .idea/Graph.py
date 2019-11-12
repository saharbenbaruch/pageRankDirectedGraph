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

    def calculate_page_rank(b, j, maxIterations):
        #init
        for node  in self.nodes:
            node.pageRank=1/(globals()['numOfNodes'])
        



class graph:
    def __init__(self):
        self.nodes={}


    def getNodes(self):
        return self.nodes



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

