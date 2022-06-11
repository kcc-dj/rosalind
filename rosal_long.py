f=open('/mnt/c/python_coding/rosalind_long.txt','r')

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
#input file arrange

def long(a1,a2):
    if len(a2)>len(a1):
        a1,a2=a2,a1
    hf=int(len(a2)/2)
    for i in range(len(a1)):
        ak2=a2[i:]
        ak1=a1[:len(ak2)]
        ad1=a1[i:]
        ad2=a2[:len(ad1)]
        if ak1==ak2:
            dd=a2[:i]+ak1
            return dd
        elif ad1==ad2:
            dd=a1[:i]+a2
            return dd

n=0

while n<1:
    dd=list()
    dj=list()
    for i in range(1,len(bb)):
        k1=long(bb[0],bb[i])
        if k1!=bb[0] and k1!=bb[i]:
            dd.append(k1)
            dj.append(len(k1))
    if not len(dj):
        print(bb[0])
        break
    else:
        dk=min(dj)
    for j in range(len(dd)):
        if len(dd[j])==dk:
            bb[0]=dd[j]
            del bb[j+1]
            break
    if len(bb)==1:
        print('bb=1')
        print(bb[0])
        break



    






