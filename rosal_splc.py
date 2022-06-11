from Bio.Seq import Seq

f=open('/mnt/c/python_coding/rosalind_splc.txt','r')
aa=f.read().split('\n')
bb=list()
cc=''
for i in aa:
    if i==aa[len(aa)-1]:
        cc+=i
        bb.append(cc)
    
    if not i.startswith('>'):
        cc+=i
    else:
        bb.append(cc)
        cc=''
bb=bb[1:]
b1=bb[0]
for i in range(1,len(bb)):
    c2=b1.replace(bb[i],'')
    b1=c2

b2=Seq(b1)
b3=Seq.translate(b2,to_stop=True)
print(b3)




