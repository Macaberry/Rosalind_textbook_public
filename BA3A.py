# Generate the k-mer Composition of a String

def Composition(k, text):
    return list(sorted([text[i:i+k] for i in range(len(text)-k+1)]))
# Input
k = 5
string = "CAATCCAAC"
# Output
print("\n".join(Composition(k,string)))

