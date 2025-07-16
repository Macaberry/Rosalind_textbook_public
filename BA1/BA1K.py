# Generate the Frequency Array of a String

def generate_all_kmer(k):
    if k == 0: return {""} # base case
    kmers = generate_all_kmer(k-1)
    subset = set()
    for kmer in kmers:
        for b in 'ATGC':
            subset.add(b + kmer)
    return subset

def freq_array(text,k):
    count = [0] * (4**k)
    kmers = sorted(generate_all_kmer(k))
    fragments = [text[i:i+k] for i in range(len(text)-k+1)]
    for frag in fragments:
        count[kmers.index(frag)] += 1
    return count

# Input 
text = "ACGCGGCTCTGAAA"
k = 2

# Output
result = freq_array(text,k)
for w in result:
    print(w,end=" ")