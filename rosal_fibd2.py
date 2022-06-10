aa=input("insert n,m\n")

aa=aa.split()
n=int(aa[0])
m=int(aa[1])

def fibd(n,m):
    bb=list()
    for i in range(1,n+1):
        
        if i==1 or i == 2:
            bb.append(1)
        elif i<=m:
            kk=bb[i-2]+bb[i-3]
            bb.append(kk)
        else:
            kk=sum(bb[i-(m+1):i-2])
            bb.append(kk)
    return bb[-1]
    

k=fibd(n,m)
print(k)
