# Construct the De Bruijn Graph of a String

def DeBruijn(k, text):
    dct = {}
    n = len(text)
    for i in range(n-k):
        dct.setdefault(text[i:i+k-1],[]).append(text[i+1:i+k])
    return dict(sorted(dct.items()))

k = 4
string = "AAGATTCTCTAC" 

result = DeBruijn(k,string)
for key, value in result.items():
    print(key+" -> "+",".join(sorted(value)))