# Find a Postition in a Genome Minimizing the Skew

def Skew(genome):
    GC_skew = [0]
    for b in genome:
        GC_skew.append(GC_skew[-1] + (1 if b=="G" else -1 if b=="C" else 0))
    return [str(idx) for idx, v in enumerate(GC_skew) if v == min(GC_skew)]
 
# Input 
genome = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"

# Output
result = Skew(genome)
print(" ".join(result))