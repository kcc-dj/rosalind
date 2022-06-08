

aa=list()
bb=list()


f=open('/mnt/c/python_coding/a.txt','r')
a=f.read().split(' ')
for i in range(len(a)):
    a1=int(a[i])
    aa.append(a1)
f.close()

f=open('/mnt/c/python_coding/b.txt','r')
a=f.read().split()
for i in range(len(a)):
    a1=int(a[i])
    bb.append(a1)
f.close()

cc=aa+bb
dd=sorted(cc)
f=open('/mnt/c/python_coding/res.txt','w')
for i in dd:
    i=str(i)
    f.write(i)
    f.write(' ')
f.close()
