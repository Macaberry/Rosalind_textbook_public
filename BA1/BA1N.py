# Generate the d-Neighborhood of a String

def Hamming_distance(str1, str2):
    return sum(1 for i,j in zip(str1, str2) if i != j)

def d_neighborhood(string, d):
    # base case
    if d == 0:
        return {string}
    if len(string) == 0:
        return {""}
    
    neighborhoods = d_neighborhood(string[1:], d)
    subset = set()
    # check Hamming_distance condition
    for kmer in neighborhoods:
        if Hamming_distance(kmer, string[1:]) < d:
            for b in 'ATGC': subset.add(b + kmer)
        else: 
            subset.add(string[0] + kmer)
    return subset

# Input 
pattern = "ACG"
k = 1

# Output
result = d_neighborhood(pattern, k)
for i in result:
    print(i)
# (added) File write
with open("BA1N_result.txt","w") as f:
    for i in result:
        f.write(i+"\n")