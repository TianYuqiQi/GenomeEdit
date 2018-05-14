#the first part
import time

print(time.ctime())

with open('chr.fa','r') as f:
    fragment = f.readlines().split(">")[1:-1]  # discard the " " in the front and end
    k = 0
    for i in fragment:
        with open("chr" + str(k) + ".fa", "w") as fw:
            fw.writelines(i)
        k += 1
#divide the original .fa into 24 .fa
def get_oneseq(chr, start, end):
    """
    this function used to get one sequence from fasta files
    """
    with open(chr + '.fa', 'r') as f:
        sequence = ''.join(f.readlines()[1:]).replace('\n', '')
        start_end_seq = sequence[start - 1:end]
        return start_end_seq

def get_seqs(fragment):
    """
    retrieve fragment from a file
    """

    f = open(fragment, 'r')
    f2 = open(fragment + '.fa', 'w')
    lists = f.readlines()[1:]
    for line in lists:
        temp = line.replace('\n', '').split('\t')
        chr = temp[0]
        start = temp[1]
        end = temp[2]
        name = temp[3]
        seq = get_oneseq(chr, int(start), int(end))
        print(f2, '>' + name + '\t' + chr + ':' + str(start) + '-' + str(end) + '\n' + seq)
    f.close()
    f2.close()


if __name__ == '__main__':
    get_seqs('fragment_file.txt')
    print(time.ctime())

