f=open('/mnt/c/python_coding/rosalind_pdst.txt','r')
aa=f.read().split('\n')
bb=list()
cc=''
for i in aa:
    if i==aa[len(aa)-1]:
        cc+=i
        bb.append(cc)
    elif not i.startswith('>'):
        cc+=i
    else:
        bb.append(cc)
        cc=''

bb=bb[1:]
kk=len(bb)
dd=[0]*kk
d2=list()
d3=list()
n=0
for i in range(kk):
    d1=list(dd)

    for j in range(kk):
        if i!=j:
            for k in range(len(bb[0])):
                if bb[i][k]!=bb[j][k]:
                    n+=1
                k1=n/len(bb[0])
                d1[j]+=k1
                n=0
            d2=[d1]
    d3+=d2

for i in range(kk):
    cc=''
    for j in range(kk):
        cc+=str(d3[i][j])
        cc+=' '
    print(cc)

     

