# Construct the De Bruijn Graph of a String

def main():
    InputFilename = "./rosalind_ba3d.txt"
    nKmer_Length, sGenome = get_Input(InputFilename)
    
    sDeBruijnDic = Construct_sDeBruijnDic(nKmer_Length, sGenome)
    
    OutputFilename = "rosalind_ba3d_result.txt"
    write_Output(OutputFilename, sDeBruijnDic)

    return 0

def Construct_sDeBruijnDic(nKmer_Length, sGenome):
    sGraphDic = {}
    nLength = len(sGenome)

    for i in range(nLength-nKmer_Length):
        sPre_kmer = sGenome[i:i+nKmer_Length-1]
        sNext_kmer = sGenome[i+1:i+nKmer_Length]

        sGraphDic.setdefault(sPre_kmer,[])

        if not sNext_kmer in sGraphDic[sPre_kmer]:
            sGraphDic[sPre_kmer].append(sNext_kmer)
    
    return dict(sorted(sGraphDic.items()))

def get_Input(filename):
    with open(filename, "r") as f:
        inputs = f.read().split()

    nKmer_Length = int(inputs[0])
    sGenome = inputs[1]

    return nKmer_Length, sGenome

def write_Output(OutputFilename, sOverlapGraphDic):
    
    with open(OutputFilename,"w") as f:
        for k,v in sOverlapGraphDic.items():
            v = sorted()
            f.write(f"{k} -> {",".join(v)}\n")
    
    return 0

if __name__ == "__main__":
    main()