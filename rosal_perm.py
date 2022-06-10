aa=int(input("insert n\n"))


def fact(n):
    if n ==1:
        return 1
    else:
        return n*fact(n-1)



def perm(n,cc):
    bb=list(range(1,n+1))
    if len(cc):
        for i in cc:
            kk=int(i)
            bb.remove(kk)
    if len(cc)==n-1:
        cc+=str(bb[0])
        c4=""
        for k in cc:
            c4+=k
            c4+=' '
        print(c4)
            
    else:
        for j in bb:
            dd=cc
            dd+=str(j)
            perm(n,dd)
   
a1=fact(aa)
dd=""
print(a1)
perm(aa,dd)

