import re
aa=input('DNA\n')
bb=input('find\n')
cc=list()
i=0
while True:
    a1=aa[i:]
    c=a1.find(bb)
    cc.append(c+1+i)
    i+=(c+1)
    if c==-1:
        break

f=open('/mnt/c/python_coding/aa.txt','w')

for i in cc:
    f.write("%s " % str(i))

f.close()


