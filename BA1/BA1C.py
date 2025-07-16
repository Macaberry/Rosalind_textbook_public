# Find the Reverse Complement of a String

def reverse_strand(pattern):
    bases = {"A":"T","G":"C","C":"G","T":"A"}
    return "".join(bases[i] for i in reversed(pattern))

# input 
pattern = "AAAACCCGGT"

# output
result = reverse_strand(pattern)
print(result)
