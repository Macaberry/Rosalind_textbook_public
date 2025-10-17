# Computing GC content

def main():
    Inputfilename = "rosalind_gc.txt"
    Outputfilename = "rosalind_gc_result.txt"

    Inputs = get_input(Inputfilename)
    Fastafilesdic = read_fastafiles(Inputs)

    GC_Storagedic = {}
    highest_GC_fasta = []
    
    for fasta_name, genomevalue in Fastafilesdic.items():
        GC_Storagedic[fasta_name] = compute_GC_content(genomevalue)
    
    highest_GC_fasta = [k for k, v in GC_Storagedic.items() if v == max(GC_Storagedic.values())]

    print_output(Outputfilename, highest_GC_fasta, GC_Storagedic)

    return 0

def get_input(filename):
    with open(filename, "r") as f:
        inputs = f.read()
    return inputs

def read_fastafiles(Fastas):
    Fastafilesdic = {}

    Inputslist = Fastas.split("\n>")
    Inputslist[0] = Inputslist[0][1:]

    for current_fasta in Inputslist:
        fastaname, genome = current_fasta.strip().split("\n", maxsplit=1)
        genome = genome.replace("\n","")
        Fastafilesdic[fastaname] = genome

    return Fastafilesdic

def compute_GC_content(sGenome):
    nGC_counts = 0

    for base in sGenome:
        if base in "GC":
            nGC_counts += 1
    
    nGC_proportion = round(nGC_counts / len(sGenome) * 100, 7)

    return nGC_proportion

def print_output(filename, highest_GC_fasta, GC_Storagedic):
    with open(filename, "w") as f:
        for fastaname in highest_GC_fasta:
            f.write(f"{fastaname}\n{GC_Storagedic[fastaname]}") 

if __name__ == "__main__":
    main()