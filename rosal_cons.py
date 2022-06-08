f=open('/mnt/c/python_coding/aa.txt','r')

gg=f.read().split('\n')

aa=list()

c1=""
for i in gg:
    if i ==gg[len(gg)-1]:
        aa.append(i)
    elif not i.startswith('>'):
        c1+=i
    else:
        aa.append(c1)
        c1=""
aa=aa[1:len(aa)]
n=len(aa[0])
print(len(aa))

A=[0]*n
C=[0]*n
G=[0]*n
T=[0]*n

for i in aa:
    for j in range(len(i)):
        if i[j]=='A':
            A[j]+=1
        elif i[j]=='C':
            C[j]+=1
        elif i[j]=='G':
            G[j]+=1
        else:
            T[j]+=1
dd=""
for i in range(n):
    k=max(A[i],C[i],G[i],T[i])
    if k==A[i]:
        dd+='A'
    elif k==C[i]:
        dd+='C'
    elif k==G[i]:
        dd+='G'
    else:
        dd+='T'


f = open('/mnt/c/python_coding/result.txt','w')
f.write(dd)
f.write('\n')
f.write('A: ')
for i in A:
    f.write('%s ' % str(i))
f.write('\n')
f.write('C: ')
for i in C:
        f.write('%s ' % str(i))

f.write('\n')
f.write('G: ')
for i in G:
        f.write('%s ' % str(i))

f.write('\n')
f.write('T: ')
for i in T:
        f.write('%s ' % str(i))
