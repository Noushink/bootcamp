start_codon = 'AUG'

seq = 'GUACGACGACGAUCAUCACCCCFCAGACGACUACGACU'
# initialize seqeunce index
i = 0
# scan the seqence until start codon
while seq [i:i+3] != start_codon:
    i += 1
print('start codon at index, i')
