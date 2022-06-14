f=open('/mnt/c/python_coding/rosalind_tran.txt','r')
aa=f.read().split('\n')

bb=list()
cc=''

for i in range(len(aa)):
    if aa[i].startswith('>'):
        bb.append(cc)
        cc=''
    else:
        cc+=aa[i]
        if i==len(aa)-1:
            bb.append(cc)

bb=bb[1:]
ts=0
tv=0
tsn=['AG','GA','TC','CT']
for j in range(len(bb[0])):
    dd=''
    if bb[0][j]!=bb[1][j]:
        dd+=bb[0][j]
        dd+=bb[1][j]
        if dd in tsn:
            ts+=1
        else:
            tv+=1

print(ts/tv)



