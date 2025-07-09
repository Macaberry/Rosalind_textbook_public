# Compute the Hamming Distance B/W two Strings

def Hamming_distance(str1, str2):
    return sum(1 for i,j in zip(str1, str2) if i != j)

# Input
string1 = "GGGCCGTTGGT"
string2 = "GGACCGTTGAC"

# Output
print(Hamming_distance(string1, string2))