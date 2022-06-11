f=open('/mnt/c/python_coding/rosalind_cons.txt','r')
aa=f.read().split('\n')
bb=list()
cc=''
for i in aa:
    if i==aa[-1]:
        cc+=i
        bb.append(cc)
    elif i.startswith('>'):
        bb.append(cc)
        cc=''
    else:
        cc+=i
f.close()
bb=bb[1:]

n=len(bb[0])
A=[0]*n
C=[0]*n
G=[0]*n
T=[0]*n

for i in bb:
    for j in range(n):
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
    mx=max(A[i],C[i],G[i],T[i])
    if mx==A[i]:
        dd+='A'
    elif mx==C[i]:
        dd+='C'
    elif mx==G[i]:
        dd+='G'
    else:
        dd+='T'
dd+='\n'
f=open('/mnt/c/python_coding/result.txt','w')
f.write(dd)
f.write('A: ')
for i in A:
    f.write('%d ' % i)
f.write('\n')
f.write('C: ')
for i in C:
    f.write('%d ' % i)
f.write('\n')
f.write('G: ')
for i in G:
    f.write('%d ' % i)
f.write('\n')
f.write('T: ')
for i in T:
    f.write('%d ' % i)





