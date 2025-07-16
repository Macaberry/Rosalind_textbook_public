# Implement NumberToPattern

def NumberToPattern(num, k):
    # convert to quarternary
    def Decimal2Quart(decimal):
        if decimal == 0: return "0"
        quart = []
        while decimal >0:
            quart.append(str(decimal % 4))
            decimal //= 4
        return "".join(reversed(quart))
    # convert to pattern
    quart = Decimal2Quart(num)
    pattern = ["A" * (k-len(quart))]
    bases = {"0":"A","1":"C","2":"G","3":"T"}
    for w in quart:
        pattern.append(bases[w])
    return "".join(pattern)

# Input
integer = 45
k = 4

# Output
print(NumberToPattern(integer,k))