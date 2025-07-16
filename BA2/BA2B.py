# Find a Median String

def HammingDistance(s1,s2):
    return sum(1 for i,j in zip(s1,s2) if i!=j)

# main
def MedianString(k, texts):
    # all possible k-mers
    def all_kmers(k):
        subset = set()
        if k == 0:
            return {""}
        tmp = all_kmers(k-1)
        for t in tmp:
            for base in 'ATGC':
                subset.add(base+t)
        return subset
    kmers = all_kmers(k)
    # count HammingDistance in dict
    dct = {}
    for pattern in kmers:
        for dna in texts:
            minhm = k # 한 dna 안의 모든 k-mer에 대해 해당 패턴의 hm 최솟값
            for mer in [dna[i:i+k] for i in range(len(dna)-k+1)]:
                if HammingDistance(mer, pattern) < minhm:
                    minhm = HammingDistance(mer, pattern)
            dct[pattern] = dct.get(pattern, 0) + minhm # loop 끝나고 해당 dna에 대한 해당 pattern의 최소 hm 업데이트
    # min d
    return [k for k,v in dct.items() if v == min(dct.values())]

# Input
with open("rosalind_ba2b.txt", "r") as f:
    inputs = f.read().splitlines()
k = int(inputs[0].strip())
strings = inputs[1:]

# Output
result = MedianString(k, strings)
print(result[0])