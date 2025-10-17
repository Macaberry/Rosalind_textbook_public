# Translate an RNA String into Amino Acid String

def main():
    InputfilePath = "./DATASET/rosalind_ba4a.txt"
    OutputfilePath = "./DATASET_RESULT/rosalind_ba4a_result.txt"

    sRNAstring = get_input(InputfilePath)

    sAAstring = convert_RNA_to_Aminoacid(sRNAstring)

    print_output(OutputfilePath, sAAstring)

    return 0

def convert_RNA_to_Aminoacid(sRNAstring):

    sAAstring = ""

    CodonTabledct = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AUG': 'M',  # Start codon
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y',
    'UAA': '*', 'UAG': '*', 'UGA': '*',  # Stop codons
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S',
    'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    sString_to_translate = None

    for i in range(len(sRNAstring)-2):

        if sRNAstring[i:i+3] == "AUG":
            sString_to_translate = sRNAstring[i:]
            break

    if sString_to_translate == None:
        return "There is no start codon."

    for j in range(0,len(sString_to_translate),3):

        current_codon = sString_to_translate[j:j+3]

        if CodonTabledct[current_codon] == "*":
            continue
        else:
            sAAstring += CodonTabledct[current_codon]
    
    return sAAstring

def get_input(FilePath):

    with open(FilePath,"r") as f:
        Inputs = f.read()
    
    return Inputs

def print_output(FilePath, result):

    with open(FilePath,"w") as f:
        f.write(result)
    
    return 0

if __name__ == "__main__":
    main()
