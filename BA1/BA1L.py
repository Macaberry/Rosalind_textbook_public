# Implement PatternToNumber

def PatternToNum(pattern):
    base_table = {"A":0,"C":1,"G":2,"T":3}
    n = len(pattern)
    i, num = 0, 0
    while i < n:
        num += base_table[pattern[i]]*(4**(n-i-1)) 
        i += 1
    return str(num) 

# Input
pattern = "CTAAGTATATGGCACCGCATACTGAG"

# Output
print(PatternToNum(pattern))