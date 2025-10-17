# Find Substrings of a Genome Encoding a Given Amico Acid String

def main():
    InputfilePath = "./DATASET/rosalind_ba4b.txt"
    OutputfilePath = "./DATASET_RESULT/rosalind_ba4b_result.txt"

    sDNAstring, sGiven_AA = get_input(InputfilePath)

    # (1) reverse_translate AA to RNA (all possible)
    PossibleRNAs_from_AA = reverse_translate_AA_to_RNAcodon(sGiven_AA)
    OriandRevPossibleRNAs_from_AA = append_reverse_string(PossibleRNAs_from_AA)

    # (2) Find each substring in RNAted DNA and its reverse strand
    Substrings_in_DNA = find_RNAcodon_in_DNAbothStrand(OriandRevPossibleRNAs_from_AA, sDNAstring)

    print_output(OutputfilePath, Substrings_in_DNA)

    return 0

def reverse_translate_AA_to_RNAcodon(sGiven_AA):

    sAllPossibleRNAs = []
    
    aa_to_codon_table = {
    'F': ['UUU', 'UUC'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'M': ['AUG'],  # Start codon
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Y': ['UAU', 'UAC'],
    '*': ['UAA', 'UAG', 'UGA'],  # Stop codons
    'H': ['CAU', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'N': ['AAU', 'AAC'],
    'K': ['AAA', 'AAG'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'C': ['UGU', 'UGC'],
    'W': ['UGG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG']
    }

    firstAA = sGiven_AA[0] 
    sAllPossibleRNAs = aa_to_codon_table[firstAA] # Initialization

    for current_AA in sGiven_AA[1:]:
    
        tmpPossibleRNAs = []

        for possible_codon in aa_to_codon_table[current_AA]:

            for former_rna in sAllPossibleRNAs:
                tmpPossibleRNAs.append(former_rna + possible_codon)
            
        sAllPossibleRNAs = tmpPossibleRNAs

    return sAllPossibleRNAs

def append_reverse_string(Originalstringlist):
    
    OriandRevstringlist = []

    for each_string in Originalstringlist:
        rev_string = make_reverse_strand_RNA(each_string)
        OriandRevstringlist.append(rev_string[::-1])

    OriandRevstringlist += Originalstringlist

    return OriandRevstringlist

def convert_RNA_to_DNA(sRNAs):
    sDNAs = [b if b != "U" else "T" for b in sRNAs]
    return "".join(sDNAs)

def make_reverse_strand_DNA(DNAstring):
    bases = {"A":"T","G":"C","C":"G","T":"A"}
    RNAstring = [bases[i] for i in DNAstring[::-1]]
    return "".join(RNAstring) # 5' > 3'

def make_reverse_strand_RNA(RNAstring):
    bases = {"A":"U","G":"C","C":"G","U":"A"}
    DNAstring = [bases[i] for i in RNAstring[::-1]]
    return "".join(DNAstring) # 5' > 3'

def find_RNAcodon_in_DNAbothStrand(GivenRNAstrings, sDNAstrand):

    Substrings_in_DNA = []
    GivenDNAstrings = []
    substring_length = len(GivenRNAstrings[0])

    for current_RNAstring in GivenRNAstrings:
        GivenDNAstrings.append(convert_RNA_to_DNA(current_RNAstring))

    # Check original strand and reverse
    for i in range(len(sDNAstrand)-substring_length+1):
            current_DNAcodon = sDNAstrand[i:i+substring_length]

            if current_DNAcodon in GivenDNAstrings:
                Substrings_in_DNA.append(current_DNAcodon)

    sDNAstrand_reverse = make_reverse_strand_DNA(sDNAstrand)[::-1]

    for i in range(len(sDNAstrand_reverse)-substring_length+1):
            current_DNAcodon = sDNAstrand_reverse[i:i+substring_length]

            if current_DNAcodon in GivenDNAstrings:
                Substrings_in_DNA.append(current_DNAcodon)
    
    return Substrings_in_DNA

def get_input(FilePath):

    with open(FilePath,"r") as f:
        Inputs = f.readlines()

    sDNAstring = Inputs[0].strip()
    sGiven_AAstring = Inputs[1].strip()
    
    return sDNAstring, sGiven_AAstring

def print_output(FilePath, sSubstrings_in_DNA):

    with open(FilePath,"w") as f:

        for current_substring in sSubstrings_in_DNA:
            f.write(f"{current_substring}\n")
    
    return 0

if __name__ == "__main__":
    main()