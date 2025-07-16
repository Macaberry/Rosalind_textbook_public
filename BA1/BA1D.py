# Find All Occurrences of a Pattern in a String

def loc_of_pattern(pattern, text):
    k = len(pattern)
    return [str(i) for i in range(len(text)-k+1) if text[i:i+k] == pattern]

# input
pattern = "ATAT"
string = "GATATATGCATATACTT"

# output
result = loc_of_pattern(pattern, string)
print(" ".join(result))
