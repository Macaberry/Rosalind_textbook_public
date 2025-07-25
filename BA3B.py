# String Spelled by a Genome Path Problem

def genomePath(patterns):
    return patterns[0] + "".join(pattern[-1] for pattern in patterns[1:])

# Input
with open("rosalind_ba3b.txt","r") as f:
    inputs = f.read().splitlines()
# Output
result = genomePath(inputs)
print(result)