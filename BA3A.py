# Generate the k-mer Composition of a String

def main():
    # Input
    inputs = get_Input(r"C:\Users\user\Desktop\Rosalind_textbook_public\rosalind_ba3a.txt")
    k = int(inputs[0])
    sString = inputs[1]

    result = Composition(k, sString)
    write_output(result)
    return 0

def Composition(k, text):
    return list(sorted([text[i:i+k] for i in range(len(text)-k+1)]))

def get_Input(filename):
    with open(filename, "r") as f:
        inputs = f.read().split()
    return inputs

def write_output(result):
    with open("rosalind_ba3a_result.txt","w") as f:
        f.write("\n".join(result))


if __name__ == "__main__":
    main()