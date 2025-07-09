# Find the Most Frequent Words with Mismathces in a String

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

def freq_words_wM(text, k, d):
    count = {}
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        for nei in d_neighborhood(kmer,d):
            if Hamming_distance(nei, kmer) <=4:
                count[nei] = count.get(nei,0) +1
    return [k for k,v in count.items() if v == max(count.values())]

# Input 
string = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

# Output
result = freq_words_wM(string,k,d)
print(" ".join(result))