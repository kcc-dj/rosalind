import math

f=open('/mnt/c/python_coding/rosalind_prob.txt','r')
a1=f.read().split('\n')
aa=a1[0]
b1=a1[1]
bb=list()
b1=b1.split()
for i in b1:
    c1=float(i)
    bb.append(c1)

result=list()

nucl=['A','T','G','C']
for i in bb:
    res=0
    val=[(1-i)/2,(1-i)/2,i/2,i/2]
    val2=dict(zip(nucl,val))
    for j in aa:
        res+=math.log10(val2[j])
    result.append(res)



f=open('/mnt/c/python_coding/result2.txt','w')
for i in result:
    f.write('%f ' % i)

f.close()
    

