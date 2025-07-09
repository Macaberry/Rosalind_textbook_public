# Find Patterns Forming Clumps in a String
## k-mers forming (L,t)-clumps in Genome

def Clump_in_Window(window,k,t):
    dct = {}
    for i in range(len(window)-k+1):
        kmer = window[i:i+k]
        dct[kmer] = dct.get(kmer,0) +1
    return [k for k,v in dct.items() if v >= t]

# input
genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
k = 5
L = 75
t = 4

# output
result = set()
for i in range(len(genome)-L+1):
    tmp = Clump_in_Window(genome[i:i+L],k,t)
    for r in tmp:
        result.add(r)
print(" ".join(result))