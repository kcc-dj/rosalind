import math

aa=input("insert k, N \n")

aa=aa.split()

k=int(aa[0])
N=int(aa[1])

tot=2**k

prob=0
for i in range(N,tot+1):
    pro=((0.25)**i)*(0.75**(tot-i)*math.comb(tot,i))
    prob+=pro
    
print(prob)


