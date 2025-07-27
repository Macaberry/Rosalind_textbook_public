# Construct the De Bruijn Graph of a Collection of k-mers

def CompositionGraph(patterns):
    dct = {}
    for p in patterns:
        dct.setdefault(p[:-1],[]).append(p[1:])
    return dict(sorted(dct.items()))

# Input
with open("rosalind_ba3e.txt","r") as f:
    inputs = f.read().splitlines()

# Output
result = CompositionGraph(inputs)
for key, value in result.items():
    print(key+" -> "+",".join(sorted(value)))