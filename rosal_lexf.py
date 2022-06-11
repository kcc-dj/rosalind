aa=input('insert collentions\n')
aa=aa.split()
bb=list(aa)
print(bb)
n=int(input('insert n\n'))
kk="o" * n


def lexf(k,dd):
    cc=list(bb)
    ss=list(dd)
    for i in cc:
        ss[k]=i
        d1=''
        for j in ss:
            d1+=j
        if k==n-1:
            print(d1)
        else:
            lexf(k+1,d1)

lexf(0,kk)
