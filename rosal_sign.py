aa=int(input('insert n\n'))

a1=list(range(1,aa+1))

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

tot=fact(aa)*(2**aa)

f=open('/mnt/c/python_coding/result.txt','w')
f.write(str(tot))
f.write('\n')

dd=list()
def perm(cc,n):
    a2=list(a1)
    cc1=list(cc)
    cc2=list(cc)
    if len(cc1)==n:
        for h in cc1:
            f.write('%d '% h)
        f.write('\n')
    elif len(cc1)==0:
        for j in a2:
            cc1.append(j)
            cc2.append(-j)
            perm(cc1,n)
            perm(cc2,n)
            cc1=list()
            cc2=list()
    else:
        for i in cc1:
            k1=abs(i)
            a2.remove(k1)
        for k in a2:
            cc1.append(k)
            cc2.append(-k)
            perm(cc1,n)
            perm(cc2,n)
            cc1=list(cc)
            cc2=list(cc)





perm(dd,aa)


    

