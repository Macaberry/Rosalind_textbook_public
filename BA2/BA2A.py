# Implement MotifEnumeration

def HammingDistance(s1,s2):
    return sum(1 for i, j in zip(s1,s2) if i != j)

def d_neighborhoods(pattern, d):
    result = set()
    if d == 0:
        return {pattern}
    if len(pattern) == 0:
        return {""}
    neighbors = d_neighborhoods(pattern[1:], d)
    for nei in neighbors:
        if HammingDistance(pattern[1:], nei) < d:
            for b in 'ATGC':
                result.add(b+nei)
        else:
            result.add(pattern[0] + nei)
    return result

    
# main
def motifenumeration(dnas, k, d):
    patterns = set()
    template = dnas.pop()
    all_neighbors = set()
    for f_mer in [template[i:i+k] for i in range(len(template)-k+1)]:
        all_neighbors = all_neighbors.union(d_neighborhoods(f_mer,d))

    for nei in all_neighbors:
        for dna in dnas: # dna string 하나씩 순회
            exist = False 
            for kmer in [dna[j:j+k] for j in range(len(dna)-k+1)]:
                if HammingDistance(nei, kmer) <= d:
                    exist = True
            if exist == False: # 하나에서 발견 안 되면 다음 nei로 skip
                break
        if exist == False:
            continue
        patterns.add(nei)

    return patterns

# Input
with open("rosalind_ba2a.txt", "r") as f:
    lines = f.read().splitlines()
k, d = map(int,lines[0].split())
text = lines[1:]

# Output
result = motifenumeration(text, k, d)
print(" ".join(result))
                    
