


def rab(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return rab(n-1)+(rab(n-2)*k)


aa=input("insert n,k\n")
aa=aa.split()

k=int(aa[1])


print(rab(int(aa[0])))



