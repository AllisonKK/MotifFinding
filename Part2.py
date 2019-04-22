import numpy as np

LOOP_TIME = 300
SEQ_LEN = 500
ALPHA = ['A', 'T', 'C', 'G']


def gibbs_sampler(sequences, motif_len):
    seq_cnt = len(sequences)
    sites = np.random.randint(0, SEQ_LEN - motif_len, seq_cnt).tolist()
    for i in range(LOOP_TIME):
        for j in range(seq_cnt):
            temp_seq = sequences[:j]+sequences[j+1:]
            temp_st = sites[:j]+sites[j+1:]
            temp_motif = get_motif(temp_seq, temp_st, motif_len)
            cur_prob = get_p(temp_motif, sequences[j], motif_len)
            sites[j] = np.random.choice(SEQ_LEN - motif_len, 1, p=cur_prob)[0]
    return sites, get_motif(sequences, sites, motif_len)


def get_motif(sequences, sites, motif_len):
    seq_cnt = len(sequences)
    motif= np.zeros([4, motif_len]) + 0.1/seq_cnt
    motif = motif.tolist()
    for i in range(seq_cnt):
        plant = sequences[i][sites[i]:sites[i]+motif_len]
        for j in range(motif_len):
            pos = ALPHA.index(plant[j])
            motif[pos][j] += 1/seq_cnt
    return motif


def get_p(motif, sequence, motif_len):
    p_a = np.prod([motif[ALPHA.index(a)][i] for i, a in enumerate(sequence[0:motif_len])])
    prob = [p_a]
    for i in range(SEQ_LEN - motif_len - 1):
        next_prob = prob[-1]* motif[ALPHA.index(sequence[i+motif_len])][-1] / motif[ALPHA.index(sequence[i])][0]
        prob.append(next_prob)
    prob = prob / np.sum(prob)
    return prob


seq = []
sequence_txt = open('benchmark/dataset5/sequences.fa')
for line in sequence_txt:
    seq.append(line.strip())
sequence_txt.close()

sts = []
sites_txt = open('benchmark/dataset5/sites.txt')
for line in sites_txt:
    sts.append(int(line.strip()))

ml = 8
print(sts)
ALPHA = ['A','T','C','G']
for i in range(5):
    print(seq[i][sts[i]:sts[i]+ml])
