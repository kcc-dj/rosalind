aa=input("insert n,m\n")

aa=aa.split()
n=int(aa[0])
m=int(aa[1])

def fibd(n,m):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n<=m:
        return fibd(n-1,m)+fibd(n-2,m)
    else:
        a1=list()
        for i in range(2,m+1):
            a1.append(fibd(n-i,m))
        return sum(a1)

k=fibd(n,m)
print(k)
