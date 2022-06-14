aa=input('insert N and x\n')
aa=aa.split()
N=int(aa[0])
x=float(aa[1])
bb=input('insert string\n')




x2=x/2

at1=0.5-x2
at=0
gc=0
for i in bb:
    if i =='A' or i=='T':
        at+=1
    else:
        gc+=1


pro=(at1**at)* (x2**gc)
npro=1-pro
print(1-(npro)**N)


