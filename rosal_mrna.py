aa=input("insert protein string\n")

prot=['F','L','S','Y','C','W','P','H','Q','R','I','M','T','N','K','V','A','D','E','G']
nrna=[2,6,6,2,2,1,4,2,2,6,3,1,4,2,2,4,4,2,2,4]

trans=dict(zip(prot,nrna))

bb=list()
for i in aa:
    cc=trans[i]
    bb.append(cc)

res=3
for j in bb:
    res=(res*j)%1000000

print(res)
