# Construct the De Bruijn Graph of a String

def main():
    
    InputFilename = "./rosalind_ba3d.txt"
    nKmer_Length, sGenome = get_Input(InputFilename)
    
    sDeBruijnDic = Construct_sDeBruijnDic(nKmer_Length, sGenome)
    
    OutputFilename = "rosalind_ba3d_result.txt"
    write_Output(OutputFilename, sDeBruijnDic)

    return 0

def Construct_sDeBruijnDic(nKmer_Length, sFullGenome):
    
    sGraphDic = {}
    nLength = len(sFullGenome)

    for i in range(nLength-nKmer_Length):
        sPre_kmer = sFullGenome[i:i+nKmer_Length-1]
        sNext_kmer = sFullGenome[i+1:i+nKmer_Length]

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

def write_Output(filename, sOverlapGraphDic):
    
    with open(filename,"w") as f:
        for k,v in sOverlapGraphDic.items():
            v = sorted()
            f.write(f"{k} -> {",".join(v)}\n")
    
    return 0

if __name__ == "__main__":
    main()