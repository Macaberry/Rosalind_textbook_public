# Find All Approximate Occurences of a Pattern in a String
def Hamming_distance(str1, str2):
    return sum(1 for i,j in zip(str1, str2) if i != j)

def appnum_of_pattern(pattern, text, d):
    lst = []
    k = len(pattern)
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        lst.append(str(i)) if Hamming_distance(kmer, pattern) <= d else None
    return lst

# Input
pattern = "ATTCTGGA"
string = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
k = 3

# Output
result = appnum_of_pattern(pattern,string,k)
print(" ".join(result))