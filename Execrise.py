def reverse_complement(seq, material = 'DNA'):
    """Compute reverse complement of a sequence."""


    rev_seq = seq[::-1]

    rev_seq = rev_seq.replace ('T', 'a')
    rev_seq = rev_seq.replace ('A', 't')
    rev_seq = rev_seq.replace ('G', 'c')
    rev_seq = rev_seq.replace ('C', 'g')

    return rev_seq



# seq.upper
# seq replace ('A', 't')
# seq replace ('T', 'a')
#seq.lower


# exercise 1.4
# seq_1 = ATCCGA
# seq_2 = ATCGCAGCCA
# range (len (seq_1))
# reverse (range (len(seq_1)))
#Longer seequence is the template.
