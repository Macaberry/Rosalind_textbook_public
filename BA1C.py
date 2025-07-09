# Find the Reverse Complement of a String

def reverse_strand(pattern):
    bases = {"A":"T","G":"C","C":"G","T":"A"}
    return reversed([bases[b] for b in pattern])

# input 
pattern = "AAAACCCGGT"

# output
result = reverse_strand(pattern)
print("".join(result))
