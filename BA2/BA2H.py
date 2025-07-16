# Implement Distance B/W pattern&strings

def HammingDistance(s1,s2):
    return sum(1 for i,j in zip(s1,s2) if i != j)

# main
def Dis_bt_PS(pattern, dna):
    k  = len(pattern)
    distance = 0
    for string in dna:
        hm = float("inf")
        for kmer in [string[i:i+k] for i in range(len(string)-k+1)]:
            new_hm = HammingDistance(pattern, kmer)
            if hm > new_hm:
                hm = new_hm
        distance += hm
    return distance

# input
with open("rosalind_ba2h.txt","r") as f:
    input = f.read().splitlines()
pattern = input[0]
texts = input[1].split()

# output
result = Dis_bt_PS(pattern, texts)
print(result)