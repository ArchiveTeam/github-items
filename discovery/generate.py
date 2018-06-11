import gzip
import os
import sys


data = [[]]
filenum = int(sys.argv[2])

def create_file(i, d):
    with open('{}_repos.txt'.format(str(i).zfill(4)), 'w') as f:
        f.write('\n'.join(['repos:{}'.format(';'.join(l)) for l in d]))

with gzip.open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if len(data[-1]) == 50:
            if len(data) == 10000:
                create_file(filenum, data)
                filenum += 1
                data = []
            data.append([])
        data[-1].append(line)

create_file(filenum, data)

