import re
f=open('/mnt/c/python_coding/rosalind_kmer.txt','r')

aa=f.read().split('\n')
cc=''
for i in range(1,len(aa)):
    cc+=aa[i]

dj='ACGT'
aa=cc

cc=''
f.close()

bb=list()
def kmer(st):
    st1=st
    for i in dj:
        n=0
        st1+=i
        if len(st1)!=4:
            kmer(st1)
        else:
            dk=countall(aa,st1,n)
            bb.append(dk)

        st1=st


def countall(a1,st,n):
    try:
        d1=a1.index(st)
        n+=1
        return countall(a1[d1+1:],st,n)

    except ValueError:
        return n

kmer(cc)
ddd=list()
for l in bb:
    j=str(l)
    ddd.append(j)

dd1=' '.join(ddd)
print(dd1)

