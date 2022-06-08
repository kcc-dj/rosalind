from Bio.Seq import Seq
aa = input("insert\n")
cc=""
for i in aa:
    cc+=i

dd=Seq(cc)
bb=dd.reverse_complement()
print(bb)
