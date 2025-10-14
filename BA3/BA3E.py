# Construct the De Bruijn Graph of a Collection of k-mers

def main():
    
    InputFilename = "rosalind_ba3e.txt"
    sKmerlist = get_Input(InputFilename)

    sDeBruijnGraph = construct_DeBruijnGraph(sKmerlist)

    OutputFilename = "rosalind_ba3e_result.txt"
    write_Output(OutputFilename, sDeBruijnGraph)

    return 0
    
def construct_DeBruijnGraph(sKmerlist):
    sDeBruijndct = {}

    for sKmer in sKmerlist:
        prefix_sKmer = sKmer[:-1]
        suffix_sKmer = sKmer[1:]

        sDeBruijndct.setdefault(prefix_sKmer,[])

        sDeBruijndct[prefix_sKmer].append(suffix_sKmer)
    
    return sDeBruijndct        

def get_Input(filename):

    with open(filename, "r") as f:
        inputs = f.read().split()

    return inputs

def write_Output(filename, sDebruinDct):
    
    with open(filename,"w") as f:
        for k,v in sDebruinDct.items():
            v = sorted(v)
            f.write(f"{k} -> {",".join(v)}\n")
    
    return 0

if __name__ == "__main__":
    main()