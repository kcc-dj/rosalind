f=open('/mnt/c/python_coding/rosalind_sseq.txt','r')

aa=f.read().split('\n')

bb=list()
cc=''
for i in range(len(aa)):
    if not aa[i].startswith('>'):
        cc+=aa[i]
        if i==len(aa)-1:
            bb.append(cc)

    else:
        bb.append(cc)
        cc=''


bb=bb[1:]

a1=bb[0]
b1=bb[1]
cc=[0]
for i in range(len(b1)):
    k1=a1.index(b1[i])+1
    a1=a1[k1:]
    k3=cc[i]
    k2=k1+k3
    cc.append(k2)
f.close()
f=open('/mnt/c/python_coding/result.txt','w')
for j in range(1,len(cc)):
    f.write('%s '% cc[j])
