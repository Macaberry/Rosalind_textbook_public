# Construct the Overlap Graph of a Collection of k-mers
from collections import defaultdict
import random

def main():
    # Input
    inputs = get_Input(r"C:\Users\user\Desktop\Rosalind_textbook_public\rosalind_ba3c.txt")
    
    sOverlapGraphDic = Make_a_OverlapGraph(inputs)

    # Output
    write_Output(sOverlapGraphDic)
    return 0

def Make_a_OverlapGraph(sKmers):
    sGraphDic = {}
    for sPreKmer in sKmers:
        sGraphDic[sPreKmer] = []
        for sNextKmer in sKmers:
            if sPreKmer[1:] == sNextKmer[:-1] and sPreKmer != sNextKmer:
                sGraphDic[sPreKmer].append(sNextKmer)
    return sGraphDic

def get_Input(filename):
    with open(filename, "r") as f:
        inputs = f.read().split()
    return inputs

def write_Output(sOverlapGraphDic):
    sOverlapGraphDic = dict(sorted(sOverlapGraphDic.items()))
    with open("rosalind_ba3c_result.txt","w") as f:
        for k,valueList in sOverlapGraphDic.items():
            if len(valueList):
                f.write(f'{k} -> {valueList[0]}\n') 

if __name__ == "__main__":
    main()