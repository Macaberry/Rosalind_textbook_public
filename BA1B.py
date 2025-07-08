# Find the Most Frequent Words in a String

def freq_words(text, k):
    dct = {}
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        dct[kmer] = dct.get(kmer,0) +1
    return [k for k, v in dct.items() if v == max(dct.values())]

# input
DNA_string = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

# output
result = freq_words(DNA_string, 4)
print(" ".join(result))