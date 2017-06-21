start_codon = 'AUG'
stop_codon = ('UAA', 'UAG', 'UGA')

codon = 'UAG'

if codon == start_codon:
    print ('This codon is the start codon.')
elif codon in stop_codon:
    print ('This is a stop codon.')
else:
    print('This is not the start codon or stop codon.')
