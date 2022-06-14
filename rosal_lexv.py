aa=input('insert strings\n')
n=int(input('insert n\n'))
bb=list()
aa=aa.split()
for i in aa:
    bb.append(i)


cc=''


def perm2(c1,n):
    c2=c1
    if len(c1)==n-1:
        for i in bb:
            c2+=i
            print(c2)
            c2=c1
    else:
        for i in bb:
            c2+=i
            print(c2)
            perm2(c2,n)
            c2=c1
        
    c1=''
     
perm2(cc,n)
