from Bio.Seq import Seq

f=open('/mnt/c/python_coding/rosalind_revp.txt','r')
bb=f.read().split()
aa=""
for i in bb:
    aa+=i


for i in range(len(aa)):
    if i+12>len(aa):
        a1=aa[i:len(aa)]
    else:
        a1=aa[i:i+12]
    for j in range(4,13):
        if j>len(a1):
            break
        b1=a1[:j]
        b2=Seq(b1)
        b3=Seq.reverse_complement(b2)
        if b1==b3:
            print('%d %d'% (i+1,j))

