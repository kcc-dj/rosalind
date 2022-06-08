
f=open('/mnt/c/python_coding/rosalind_ins.txt','r')
bb=f.read().split(' ')
aa=list(bb)
f.close()
a=list()
for i in range(len(aa)):
    c=int(aa[i])
    a.append(c)

n=0
for i in range(1,len(a)):
    k=i
    while k>=1 and a[k]<a[k-1]:
        a[k],a[k-1]=a[k-1],a[k]
        n+=1
        k=k-1
print(n)


