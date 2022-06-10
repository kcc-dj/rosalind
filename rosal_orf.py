from Bio.Seq import Seq


aa=input("insert DNA\n")

bb=aa.replace('T','U')

dd=list()

for i in range(len(bb)):
    cc=bb[i:]
    if cc.startswith('AUG'):
        c1=Seq(cc)
        c2=Seq.translate(c1,to_stop=True)
        dd.append(c2) 
ee=set(dd)
for i in ee:
    print(i)
