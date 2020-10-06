import argparse

def readSif(fn):
    """reads in the sif file fn and ouptputs a 
    dictionary and a list:
    interDict : has "interaction" as key 
    and [(node1,node2), (node3,node4)] as values 
    nodes list : is the list of unique node names 
    (both on the right or left hand of an interaction)
    """
    interDict = {}
    nodes = []
    with open(fn, "r") as myfile:
        for line in myfile:
            line = line.strip()
            [n1,inter,n2] = line.split("\t")
            if inter not in interDict:
                interDict[inter] = [(n1,n2)]
            else:
                interDict[inter].append((n1,n2))
            
            if n1 not in nodes:
                nodes.append(n1)
            if n2 not in nodes:
                nodes.append(n2)
    
    return interDict,nodes

def getMostPresentInteraction(iDict):
    """gets the interaction dictionary as defined above and returns the
    most present interaction (with its count). If more than one, all are
    returned comma separated"""
    mpInter = ""
    mpInterCount = 0
    for inter in iDict:
        
        cnt = len(iDict[inter])
        
        if mpInterCount < cnt:
            mpInterCount = cnt
            mpInter = inter
        elif mpInterCount == cnt:
            mpInterCount = cnt #not necessary
            mpInter = mpInter + "," + inter
    return (mpInter,mpInterCount)

def getMostPresentNode(iDict, nodeList):
    """gets the most highly connected node (or nodes, comma separated)
    and returns it with its count
    iDict : the interaction dictionary seen above
    nodeList : the node of unique node names seen above
    """
    mostPresentNode = ""
    mostPresentCount = 0
    #NOTE: iDict : {"inter1" : [(n1,n2), (n2,n3),(n3,n1), (n1,n3)], 
    #               "inter2" : [(n5,n1), (n1,n2)] }
    #
    for n in nodeList:
        #the number of times a node is present is the sum of its count 
        #in all interactions
        #both as first or second member of the couple
        curCnt = 0
        for i in iDict:
            pairsContainingN = [x for x in iDict[i] if n in x]
            curCnt = curCnt + len(pairsContainingN)
        if(curCnt > mostPresentCount):
            mostPresentNode = n
            mostPresentCount = curCnt
        elif curCnt == mostPresentCount:
            postPresentNode += "," + n
            mostPresentCount = curCnt
    
    return (mostPresentNode,mostPresentCount)
            
parser = argparse.ArgumentParser(description="""Reads and processes a .sif file""")
parser.add_argument("filename", type=str, help="The .sif file name")

args = parser.parse_args()
inputFile = args.filename
#inputFile = "file_samples/pka.sif"
interactions, nodeL = readSif(inputFile)
(mpI,mpICount) = getMostPresentInteraction(interactions)
print("The most present interaction(s): {}. Present {} times".format(mpI,mpICount))
(mpN, mpNCount) = getMostPresentNode(interactions,nodeL)
print("The most present node(s) {}. Present {} times".format(mpN,mpNCount))
