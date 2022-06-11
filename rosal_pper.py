def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

def perm(n1,n2):
    d1=fact(n1)
    d2=fact(n1-n2)
    return d1/d2


aa=input('insert n,k\n')
aa=aa.split()
n=int(aa[0])
k=int(aa[1])

perm1=perm(n,k)

print(perm1%1000000)
    
