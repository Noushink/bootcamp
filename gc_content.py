seq = 'GACAGACUCCAUGCACGUGGGUAUCUGUC'

#Initialize the GC counter
n_gc = 0
# loop through the sequences and count G's and C's
for base in seq:
    if base in 'GCgc':
        n_gc += 1
print(n_gc / len(seq))
