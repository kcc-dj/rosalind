from Bio import SeqUtils
from Bio.Seq import Seq

f=open('/mnt/c/python_coding/rosalind_gc.txt')
aa=f.read().split('\n')
ros=list()
seq=list()
cc=""
for i in aa:
    if i ==aa[len(aa)-1]:
        cc+=i
        seq.append(cc)
    if i.startswith('>'):
        a1=i.strip('>')
        ros.append(a1)
        seq.append(cc)
        cc=""
    else:
        cc+=i

seq=seq[1:len(aa)]



for i in range(len(seq)):
    se1=Seq(seq[i])
    kk=SeqUtils.GC(se1)
    print(ros[i],kk)


