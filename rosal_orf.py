from Bio.Seq import Seq


aa=input('insert DNA string\n')
stop=['TAA','TAG','TGA']

res=list()
def orf(st):
    for i in range(len(st)):
        bb=list()
        a1=st[i:]
        if a1.startswith('ATG'):
            for k in range(len(a1)//3):
                bb.append(a1[3*k:3*(k+1):])
            for j in stop:
                if j in bb:
                    b1=Seq(a1)
                    b2=Seq.translate(b1,to_stop=True)
                    res.append(b2)
                    break

orf(aa)
a3=Seq(aa)
a4=Seq.reverse_complement(a3)
a3=str(a4)
orf(a3)
dd=set(res)
for i in dd:
    print(i)
