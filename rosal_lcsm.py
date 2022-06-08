f=open('/mnt/c/python_coding/aa.txt','r')
aa=f.read().split('>Rosalind_')

bb=list()
for i in aa:
    i2=i[4:]
    bb.append(i2.replace('\n',''))

bb=bb[1:]

def find_str(a1,a2):
    if len(a2) > len(a1):
        a2,a1=a1,a2
    for i in range(len(a2)):
        for j in range(i+1):
            kk=a2[j:len(a2)-i+j]
            if kk in a1:
                return kk

cmstr="A"
for i in range(len(bb)-1):
    a1=bb[i]
    a2=bb[i+1]
    st=find_str(a1,a2)
    if st !=None:
        if len(st)>len(cmstr):
            cmstr=st

print(cmstr)


