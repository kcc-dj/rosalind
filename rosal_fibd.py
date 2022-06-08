aa=input("insert n,m\n")

aa=aa.split()
n=int(aa[0])
m=int(aa[1])

def fibd(n,m):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n<=l:
        return fibd(n-1)+fibd(n-2)
    else:
        a1=list()
        for i in range(2,l+1):
            a1.append(fibd(n-i))
        return sum(a1)

k=fibd(n)
print(k)
