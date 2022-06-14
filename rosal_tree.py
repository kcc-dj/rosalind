f=open('/mnt/c/python_coding/rosalind_tree.txt','r')
aa=f.read().split('\n')
n=int(aa[0])
n1=list(range(1,n+1))
bb=list()
dd=list()
for i in range(1,len(aa)):
    cc=aa[i].split()
    dd=list()
    dd.append(cc[0])
    dd.append(cc[1])
    bb+=dd
    for i in dd:
        h1=int(i)
        if h1 in n1:
            n1.remove(h1)


m=0

while True:
    b1=list()
    b1.append(bb[0])
    b1.append(bb[1])
    del bb[0]
    del bb[0]
    j=0
    while True:
        if len(bb)==0:
            break
        else:

            k0=bb[2*j]
            k1=bb[2*j+1]
            if k0 in b1 or k1 in b1:
                b1.append(k0)
                b1.append(k1)
                del bb[2*j]
                del bb[2*j]
                j=0
            else:
                j+=1
                if j>=len(bb)//2:
                    break
    m+=1
    if not len(bb):
        break

print(m+len(n1)-1)



    




