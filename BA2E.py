# Find a Profile-most Probable k-mer in a String

def prob_of(kmer,matrix):
    prob = 1
    dct = {"A":0,"C":1,"G":2,"T":3}
    for s in range(len(kmer)):
        prob *= matrix[dct[kmer[s]]][s] # [base][position]
    return prob

def profile_kmer(text, k, matrix):
    all_kmers = [text[i:i+k] for i in range(len(text)-k+1)]
    kmerprob = {kmer:0 for kmer in all_kmers}
    for kmer in all_kmers:
        if kmerprob[kmer] > prob_of(kmer,matrix):
            continue
        kmerprob[kmer] = prob_of(kmer,matrix)
    return [k for k,v in kmerprob.items() if v == max(kmerprob.values())]

            

# Input
with open("rosalind_ba2c.txt", "r") as f:
    inputs = f.read().splitlines()
text = inputs[0]
k = int(inputs[1])
matrix = [] # 4*k matrix
for l in inputs[2:]:
    matrix.append(list(map(float,l.split())))

# Output
result = profile_kmer(text,k,matrix)
print(result[0])