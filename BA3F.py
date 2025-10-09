# Find an Eulerian Cycle in a Graph

def main():
    
    InputFilename = "rosalind_ba3f.txt"
    nGraphdct = get_Input(InputFilename)

    sEulerainCycle = FindEulerianCircuit(nGraphdct)

    OutputFilename = "rosalind_ba3f_result.txt"
    write_Output(OutputFilename, sEulerainCycle)

    return 0
    
def FindEulerianCircuit(nGraphdct):
    circuit = []
    currentNodestack = []

    startNode = next(iter(nGraphdct.keys()))
    
    currentNodestack.append(startNode)
    
    while currentNodestack:
        
        currentNode = currentNodestack[-1]

        if nGraphdct[currentNode]:
            neighborNode = nGraphdct[currentNode].pop()
            currentNodestack.append(neighborNode)
        else:
            circuit.append(currentNode)
            currentNodestack.pop()

    if nGraphdct == True:
        return "No Eulerain Cycle"
    else: 
        return list(reversed(circuit))


def get_Input(filename):

    with open(filename, "r") as f:
        sInputlines = f.readlines()

    nAdjacencydct = {}

    for sEachLine in sInputlines: # processing to adjacency list
        nStartNode, nEndNodelist = sEachLine.split("->")

        nStartNode = int(nStartNode)
        nEndNodelist = list(map(int, nEndNodelist.split(",")))

        nAdjacencydct.setdefault(nStartNode, nEndNodelist)
        
    return nAdjacencydct

def write_Output(filename, sEulerainCycle):
    
    with open(filename,"w") as f:
        cycleLength = len(sEulerainCycle)
        for i in range(cycleLength):
            if i == cycleLength-1:
                f.write(str(sEulerainCycle[i]))
                break
            f.write(f"{str(sEulerainCycle[i])}->")
    
    return 0

if __name__ == "__main__":
    main()