aa=input('insert six integers\n')

aa=aa.split()
bb=list()
for i in aa:
    a1=int(i)
    bb.append(a1)

print(2*(sum(bb[:3])+(0.75*bb[3])+(0.5*bb[4])))
