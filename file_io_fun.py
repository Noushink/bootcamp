import os

if os.path.isfile('mastery.txt'):
    raise RuntimeError('File mastery.txt already exists.')
    print ('Sorry, file exists.')
else:
    with open('mastery.txt', 'w') as f:
        f.write('This is my file.\n')
        f.write('There are many life it, but this one is mine.\n')
        f.write('I must master my file like I must master my life.\n')
