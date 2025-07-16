# Compute the Numbeer of Times a Pattern Appears in a Text

def PatternCount(text, pattern):
    k = len(pattern)
    return sum(text[i:i+k] == pattern for i in range(len(text)-k+1))

# input
text = "GCGCG"
pattern = "GCG"

# output
result = PatternCount(text,pattern)
print(result)