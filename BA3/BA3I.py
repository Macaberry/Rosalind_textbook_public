# Fina a k-Universal Circular String
from collections import defaultdict

def main():

    InputFilename = "rosalind_ba3i.txt"
    integer_k = get_Input(InputFilename)   

    # (1) Construct De Bruijn Graph for integer_k
    sDebruijn_strings = make_deBruijnGraph_for_length_k_binary(integer_k)
    sEdges_in_graph = make_edge_list(sDebruijn_strings)

    # (2) Find Eulerian Cycle and convert to string
    sRawEulerCycle = find_eulerian_path(sEdges_in_graph)
    s_k_Universial_Circular_string = convert_eulerpath_to_string_for_circularstring(sRawEulerCycle,integer_k)

    OutputFilename = "rosalind_ba3i_result.txt"
    write_Output(OutputFilename, s_k_Universial_Circular_string)
    return 0

def make_deBruijnGraph_for_length_k_binary(integer_k):
    
    sBinarydebruijn = defaultdict(list)
    sDebruijn_strings = []

    def recursive_kmer_production_binary(k):
        if k < 1:
            return [""]
    
        former_kmerlist = recursive_kmer_production_binary(k-1)
        current_kmerlist = []

        for current_kmer in former_kmerlist:    
            for seed in "01":
                current_kmerlist.append(current_kmer+seed)
        return current_kmerlist
    
    sKmers = recursive_kmer_production_binary(integer_k)
    
    for sKmer in sKmers:
        Prefix, Suffix = sKmer[:-1], sKmer[1:]

        if not Suffix in sBinarydebruijn[Prefix]:
            sBinarydebruijn[Prefix].append(Suffix)

    for prefix_key in iter(sBinarydebruijn.keys()):
        for suffix_value in sBinarydebruijn[prefix_key]:
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

def convert_eulerpath_to_string_for_circularstring(sRawEulerpath,k):
    sFinalstring = sRawEulerpath[0]

    for sKmernode in sRawEulerpath[1:-1]:
        sFinalstring += sKmernode[-1]

    def count_zero(string):
        n = 0
        for chr in string:
            if chr == "0":
                n += 1
            else:
                break
        return n

    nPre_zeros = count_zero(sFinalstring)
    nSuf_zeros = count_zero(sFinalstring[::-1])

    if (nPre_zeros + nSuf_zeros) > k:
        difference = nPre_zeros + nSuf_zeros - k
        sFinalstring = sFinalstring[:-difference]

    return sFinalstring

def get_Input(filename):

    with open(filename, "r") as f:
        sInput = f.read()
    
    integer_k = int(sInput.strip())

    return integer_k

def write_Output(filename, sGenomeString):
    
    with open(filename,"w") as f:
        f.write(sGenomeString)
    
    return 0

if __name__ == "__main__":
    main()