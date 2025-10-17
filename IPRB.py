# Mendel's First Law

def main():
    Inputfilename = "rosalind_iprb.txt"
    Outputfilename = "rosalind_iprb_result.txt"

    nDominant_homo, nHetero, nRecessive_homo = map(int, get_input(Inputfilename).split())

    fProb_result = compute_prob_of_dominantallele(nDominant_homo, nHetero, nDominant_homo)

    print_output(Outputfilename, fProb_result)

    return 0

def compute_prob_of_dominantallele(nDominant_homo, nHetero, nRecessive_homo):
    nPopulation = nDominant_homo + nHetero + nRecessive_homo
    fProb_for_select_two = nPopulation*(nPopulation-1)/2
    # case 1
    fRevProb1 = nRecessive_homo*(nRecessive_homo-1)/2 /fProb_for_select_two
    # case 2
    fRevProb2 = nHetero*(nHetero-1)/2 /fProb_for_select_two /2/2 + nHetero*nRecessive_homo/fProb_for_select_two /2
    
    fProb_result = 1-fRevProb1-fRevProb2

    return fProb_result

def get_input(filename):
    with open(filename, "r") as f:
        inputs = f.read()
    return inputs

def print_output(filename, fProb_result):

    with open(filename, "w") as f:
        f.write(str(round(fProb_result, 5)))

if __name__ == "__main__":
    main()