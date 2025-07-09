# Find Frequent Words with Mismatches and Reverse Complements

def Hamming_distance(str1, str2):
    return sum(1 for i,j in zip(str1, str2) if i != j)

def d_neighborhood(string, d):
    if d == 0: # base case
        return {string}
    if len(string) == 0:
        return {""}
    
    subset = set() # chech HD and make set
    for kmer in d_neighborhood(string[1:], d):
        if Hamming_distance(kmer, string[1:]) < d:
            for b in 'ATGC': subset.add(b + kmer)
        else: 
            subset.add(string[0] + kmer)
    return subset

def reverse_strand(pattern):
    bases = {"A":"T","G":"C","C":"G","T":"A"}
    return "".join(bases[i] for i in reversed(pattern))

# main
def freq_words_wM_reverse(text, k, d):
    count = {}
    n = len(text)
    for i in range(n-k+1):
        kmer = text[i:i+k]
        for nei in d_neighborhood(kmer,d):
            count[nei] = count.get(nei,0) +1
        for rev_nei in d_neighborhood(reverse_strand(kmer),d):
            count[rev_nei] = count.get(rev_nei,0) +1
        
    return [k for k,v in count.items() if v == max(count.values())]

# Input 
string = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

# Output
result = freq_words_wM_reverse(string,k,d)
print(" ".join(result))