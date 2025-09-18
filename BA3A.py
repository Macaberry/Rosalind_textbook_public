# Generate the k-mer Composition of a String

def main():
    # Input
    k = 5
    sString = "CAATCCAAC"

    # Output
    result = Composition(k, sString)
    print("\n".join(result))

def Composition(k, text):
    return list(sorted([text[i:i+k] for i in range(len(text)-k+1)]))

if __name__ == "__main__":
    main()