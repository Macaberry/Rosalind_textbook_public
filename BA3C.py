# Construct the Overlap Graph of a Collection of k-mers

def Overlap(patterns):
    # (1) store prefix first for O(n)
    pre_dct = {}
    for pattern in patterns:
        pre_dct.setdefault(pattern[:-1],[]).append(pattern)
    # (2) find each suffix in pre_dct
    overlaplist = []
    for p_suf in patterns:
        if p_suf[1:] in pre_dct:
            for p_pre in  pre_dct[p_suf[1:]]:
                if p_suf != p_pre:                 
                    overlaplist.append((p_suf, p_pre))
    return sorted(overlaplist)

# Input
with open("rosalind_ba3c.txt","r") as f:
    inputs = f.read().splitlines()
# Output
result = Overlap(inputs)
for i in range(len(result)):
    print(result[i][0]+" -> "+result[i][1])