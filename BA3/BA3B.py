# String Spelled by a Genome Path Problem

def main():
    # Input
    inputs = get_Input(r"C:\Users\user\Desktop\Rosalind_textbook_public\rosalind_ba3b.txt")
    sKmers = inputs

    result = Reconstruct_Str_from_kmers(sKmers)

    # Output
    write_Output(result)
    return 0

def Reconstruct_Str_from_kmers(sKmers):
    sGenome = sKmers[0]
    for sKmer in sKmers[1:]:
        sGenome += sKmer[-1]
    return sGenome

def get_Input(filename):
    with open(filename, "r") as f:
        inputs = f.read().split()
    return inputs

def write_Output(result):
    with open("rosalind_ba3b_result.txt","w") as f:
        f.write(result)

if __name__ == "__main__":
    main()