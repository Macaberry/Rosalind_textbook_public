# Construct a String Spelled by a Gapped Genome Path

# Reconstruct a String from its Paired Composition

from collections import defaultdict

def main():
    
    InputFilename = "rosalind_ba3l.txt"
    int_k, gap_d, sPairedKmers = get_Input(InputFilename)

    # assmble each Kmerlist to Genome
    sDebruijngraph_paired = make_deBruijnGraph_paired(int_k, sPairedKmers)

    edges = make_edge_list_paired(sDebruijngraph_paired)
    sRawEulerpath_paired = find_eulerian_path_paired(edges)
    
    sFinalstring1, sFinalstring2 = convert_eulerpath_to_string_paired(sRawEulerpath_paired)

    # assemble strings to one
    sAssembledString = assemble_paired_to_oneString(int_k, gap_d, sFinalstring1, sFinalstring2)

    OutputFilename = "rosalind_ba3l_result.txt"
    write_Output(OutputFilename, sAssembledString)

    return 0
    
def find_eulerian_path_paired(edges):
    graph = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)

    # Construct a directed graph
    for u,v in edges: 
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
        if graph[u]:    
            v = graph[u].pop()
            stack.append(v)
        else:
            path.append(stack.pop())

    return path[::-1]

def make_deBruijnGraph_paired(int_k, sPairedKmers):
    
    sGraphDic_paired = defaultdict(list)
    
    for sPaired_Kmer in sPairedKmers:
        FirstKmer, SecondKmer = sPaired_Kmer

        Prefix1, Suffix1 = FirstKmer[:-1], FirstKmer[1:]
        Prefix2, Suffix2 = SecondKmer[:-1], SecondKmer[1:]

        if not (Suffix1, Suffix2) in sGraphDic_paired[(Prefix1,Prefix2)] :
            sGraphDic_paired[(Prefix1,Prefix2)].append((Suffix1, Suffix2))

    return sGraphDic_paired

def make_edge_list_paired(sRawDebruijn_paired):
    edges = []
    
    for sPairedVertex1, sPairedVertex2list in sRawDebruijn_paired.items(): 
        
        for sCurrent_vertex2 in sPairedVertex2list:
            edges.append((sPairedVertex1, sCurrent_vertex2))

    return edges

def convert_eulerpath_to_string_paired(sRawEulerpath_paired):
    sFinalstring1, sFinalstring2 = sRawEulerpath_paired[0]

    for sKmernode1, sKmernode2 in sRawEulerpath_paired[1:]:
        sFinalstring1 += sKmernode1[-1]
        sFinalstring2 += sKmernode2[-1]

    return sFinalstring1, sFinalstring2

def assemble_paired_to_oneString(int_k, gap_d, sFinalstring1, sFinalstring2):
    
    length = len(sFinalstring1) - int_k - gap_d

    sAssembledString = sFinalstring1
    
    for i in range(int_k+gap_d+1):
        if sAssembledString[-length:] == sFinalstring2[i:i+length]:
            sAssembledString += sFinalstring2[i+length:]
            continue

    return sAssembledString

def get_Input(filename):

    with open(filename, "r") as f:
        sInputlines = f.readlines()
    
    int_k, gap_d = map(int, sInputlines[0].split())

    sPairedKmers = [tuple(paired_kmer.strip().split("|")) for paired_kmer in sInputlines[1:]]

    return int_k, gap_d, sPairedKmers

def write_Output(filename, sAssembledString):
    
    with open(filename,"w") as f:
        f.write(sAssembledString)
    
    return 0

if __name__ == "__main__":
    main()