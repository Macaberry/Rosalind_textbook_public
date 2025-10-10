# Find an Eulerian Path in Graph
from collections import defaultdict

def main():
    
    InputFilename = "rosalind_ba3g.txt"
    edges = get_Input(InputFilename)    # (u,v)

    nEulerianPathlist = find_eulerian_path(edges)

    OutputFilename = "rosalind_ba3g_result.txt"
    write_Output(OutputFilename, nEulerianPathlist)

    return 0
    
def find_eulerian_path(edges):
    graph = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)

    # Construct a directed graph
    for u, v in edges: 
        graph[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1

    # find start vertex
    start = None
    for v in set(in_deg) | set(out_deg):
        if out_deg[v] - in_deg[v] == 1:
            start = v
            break
    if start is None:       # case for Eulerain Circuit 
        start = next(iter(graph))

    # Hierholzer's algorithm
    path, stack = [], [start]
    while stack:
        u = stack[-1]
        if graph[u]:    # 해당 vertex와 이어지는 vertexes가 있으면
            v = graph[u].pop()
            stack.append(v)
        else:
            path.append(stack.pop())

    return path[::-1]


def get_Input(filename):

    with open(filename, "r") as f:
        sInputlines = f.readlines()

    edges = []
    
    for sEachLine in sInputlines: 
        nVertex1, nVertex2list = sEachLine.split("->")
        nVertex1 = int(nVertex1)
        nVertex2list = list(map(int, nVertex2list.split(","))) # can have multiple value

        for nCurrent_vertex2 in nVertex2list:
            edges.append((nVertex1, nCurrent_vertex2))
        
    return edges

def write_Output(filename, nEulerianPathlist):
    
    with open(filename,"w") as f:
        nLength = len(nEulerianPathlist)
        for i in range(nLength):
            if i == nLength-1:
                f.write(str(nEulerianPathlist[i]))
                break
            f.write(f"{str(nEulerianPathlist[i])}->")
    
    return 0

if __name__ == "__main__":
    main()