# Implement GibbsSampler
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

def cumulative_rand_motif(string, k, profile):
    # string의 k-mer 마다 누적확률 계산
    cumul_prob = []
    current_prob = 0
    kmers = [string[i:i+k] for i in range(len(string)-k+1)]
    for kmer in kmers:
        current_prob += prob_of(kmer, profile)
        cumul_prob.append(current_prob)
    random_num = random.uniform(0,current_prob)
    for m in range(len(string)-k+1):
        if random_num < cumul_prob[m]:
            return kmers[m]

# main
def GibbsSampler(dnas,k,t,N):
    motifs = []
    for m in range(t):
        motifs.append(random.choice([dnas[m][n:n+k] for n in range(len(dnas[m])-k+1)]))
    bestmotifs = motifs
    for j in range(1, N):
        i = random.randint(0,t-1)
        motifs.pop(i)
        profile = make_pseudo_profile(motifs)
        # profile 확률 기반 누적확률 motif 랜덤 선택
        motif = cumulative_rand_motif(dnas[i], k, profile)
        motifs.insert(i, motif)
        if score_motifs(motifs) < score_motifs(bestmotifs):
            bestmotifs = motifs
    return bestmotifs
    
# Input 
with open("rosalind_ba2g.txt","r") as f:
    inputs = f.read().splitlines()
k,t,N = map(int,inputs[0].split())
strings = inputs[1:]

# Output 
bestmotif = ""
bestscore = float("inf")
for _ in range(20):
    result = GibbsSampler(strings,k,t,N)
    if score_motifs(result) < bestscore:
        bestscore = score_motifs(result)
        bestmotif = result

print("\n".join(bestmotif))