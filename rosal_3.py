
f=open('/mnt/c/python_coding/1.txt','r')
bb=f.read().split(' ')
aa=list(bb)
f.close()

a1=list(aa)

f=open('/mnt/c/python_coding/2.txt','r')
bb=f.read().split(' ')
aa=list(bb)
f.close()
b1=list(aa)
cc=list()
for b in b1:
    try:
        c=a1.index(b)
        cc.append(c)
    except ValueError:
        cc.append(-1)



print(len(a1)) 
print(len(b1))
print(len(cc))
f=open('/mnt/c/python_coding/res.txt','w')
for i in cc:
    i=str(i)
    f.write(i)
    f.write(' ')
f.close()

