# Implement PatternToNumber

def PatternToNum(pattern):
    base_table = {"A":0,"C":1,"G":2,"T":3}
    decimal = sum(base_table[i] for i in pattern)
    def decimal2quart(num):
        if num == 0: return '0'
        lst = []
        while num > 0:
            lst.append(str(num % 4))
            num //= 4
        return "".join(reversed(lst))
    return decimal2quart(decimal)

# Input
pattern = "AGT"

# Output
print(PatternToNum(pattern))