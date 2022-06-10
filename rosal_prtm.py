f = open('/mnt/c/python_coding/protein_weight.txt','r')
aa=f.read().split('\n')

pro=list()
wei=list()

for i in aa:
    a1=i.split()
    pro.append(a1[0])
    a2=float(a1[1])
    wei.append(a2)

prot_wei=dict(zip(pro,wei))

f.close()

bb=input("insert proteins\n")
total=0
for i in bb:
    total+=prot_wei[i]

print(total)



