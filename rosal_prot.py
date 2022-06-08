from Bio.Seq import Seq


aa=open('/mnt/c/python_coding/prot.txt','r')
a3=aa.read()
a1=Seq(a3)
a2=Seq.translate(a1,to_stop=True)
print(a2)
aa.close()
