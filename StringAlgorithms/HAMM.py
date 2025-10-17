def main():
    Inputfilename = "rosalind_hamm.txt"
    Outputfilename = "rosalind_hamm_result.txt"

    String1, String2 = get_input(Inputfilename).split()

    nHammingdistance = compute_hammingdistance_of_two(String1, String2)
    
    print_output(Outputfilename, nHammingdistance)

    return 0

def compute_hammingdistance_of_two(String1, String2):
    return sum([1 for base1, base2 in zip(String1, String2) if base1 != base2])

def get_input(filename):
    with open(filename, "r") as f:
        inputs = f.read()
    return inputs

def print_output(filename, nHammingdistance):

    with open(filename, "w") as f:
        f.write(str(nHammingdistance))

if __name__ == "__main__":
    main()