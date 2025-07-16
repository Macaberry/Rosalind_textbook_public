# Implement RandomizedMotifSearch
import random

def make_pseudo_profile(strings): # strings = ["ATG","GGG","GTC",...]
    matrix = [] # [{dct1},{dct2}, ...]
    n = len(strings) # num of kmers
    k = len(strings[0]) # length of k-mer
    for i in range(k): # for each position
        dct = {"A":1.0,"C":1.0,"G":1.0,"T":1.0}
        for j in range(n):
            dct[strings[j][i]] += 1.0
        matrix.append({b:(dct[b]/(n+4.0)) for b in 'ACGT'})
    return matrix  

def prob_of(kmer,profile):
    prob = 1.0
    for s in range(len(kmer)):
        prob *= profile[s][kmer[s]] # [position][base]
    return prob

def profile_most_kmer(text, k, profile):
    max_prob = -1
    best_kmer = text[0:k]
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        p = prob_of(kmer, profile)
        if p > max_prob:
            max_prob = p
            best_kmer = kmer
    return best_kmer

def score_motifs(motifs): # consensus score, 복습필요
    k = len(motifs[0])
    consensus = ""
    for j in range(k):
        count = {"A":0, "C":0, "G":0, "T":0}
        for motif in motifs:
            count[motif[j]] += 1
        consensus += max(count, key=count.get)
    score = 0
    for motif in motifs:
        for i in range(k):
            if motif[i] != consensus[i]:
                score += 1
    return score

def profile_updated_motifs(texts, k, profile):
    motifs = []
    for i in range(len(texts)): # each i-th string
        motifs.append(profile_most_kmer(texts[i], k, profile))
    return motifs

# main
def RandomizedMotifSearch(dnas,k,t):
    motifs = []
    for m in range(t):
        motifs.append(random.choice([dnas[m][n:n+k] for n in range(len(dnas[m])-k+1)]))
    bestmotifs = motifs
    while True:
        profile = make_pseudo_profile(motifs)
        motifs = profile_updated_motifs(dnas, k, profile)
        if score_motifs(motifs) < score_motifs(bestmotifs):
            bestmotifs = motifs
        else: return bestmotifs

# Input
with open("rosalind_ba2f.txt","r") as f:
    inputs = f.read().splitlines()
k, t = map(int, inputs[0].split())
strings = inputs[1:]

# Output
best_result = None
best_score = float("inf")
for _ in range(1000):
    motifs = RandomizedMotifSearch(strings,k,t)
    s = score_motifs(motifs)
    if s < best_score:
        best_score = s
        best_result = motifs
print("\n".join(best_result))