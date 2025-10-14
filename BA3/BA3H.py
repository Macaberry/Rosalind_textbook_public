# Reconstruct a String from its k-mer Composition
from collections import defaultdict

def main():
    
    InputFilename = "rosalind_ba3h.txt"
    k, sKmerslist = get_Input(InputFilename)   
    # make a graph 
    sRawDebruijngraph = make_deBruijnGraph(k, sKmerslist)
    sEdgeslist = make_edge_list(sRawDebruijngraph)
    
    sRawEulerpath = find_eulerian_path(sEdgeslist)
    sGenomeString = convert_eulerpath_to_string(sRawEulerpath)

    OutputFilename = "rosalind_ba3h_result.txt"
    write_Output(OutputFilename, sGenomeString)

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

def make_deBruijnGraph(nKmer_Length, sKmers):
    
    sGraphDic = defaultdict(list)
    sDebruijn_strings = []
    
    for sKmer in sKmers:
        sKmer = sKmer.strip()
        Prefix, Suffix = sKmer[:-1], sKmer[1:]
        if not Suffix in sGraphDic[Prefix]:
            sGraphDic[Prefix].append(Suffix)

    for prefix_key in iter(sGraphDic.keys()):
        for suffix_value in sGraphDic[prefix_key]:
            sDebruijn_strings.append(f"{prefix_key}->{suffix_value}")

    return sDebruijn_strings

def make_edge_list(sInputlines):
    edges = []
    
    for sEachLine in sInputlines: 
        sVertex1, sVertex2list = sEachLine.split("->")
        sVertex2list = sVertex2list.split(",") # can have multiple value

        for sCurrent_vertex2 in sVertex2list:
            edges.append((sVertex1, sCurrent_vertex2))

    return edges

def convert_eulerpath_to_string(sRawEulerpath):
    sFinalstring = sRawEulerpath[0]

    for sKmernode in sRawEulerpath[1:]:
        sFinalstring += sKmernode[-1]

    return sFinalstring

def get_Input(filename):

    with open(filename, "r") as f:
        sInputlines = f.readlines()
    
    k = int(sInputlines[0])
    sKmers = [kmer.strip() for kmer in sInputlines[1:]]

    return k, sKmers

def write_Output(filename, sGenomeString):
    
    with open(filename,"w") as f:
        f.write(sGenomeString)
    
    return 0

if __name__ == "__main__":
    main()