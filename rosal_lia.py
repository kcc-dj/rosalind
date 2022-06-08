aa=input("insert k, N \n")

aa=aa.split()

k=int(aa[0])
N=int(aa[1])

tot=2**k

prob=0
for i in range(N):
    if i==0:
        pro=(0.75)**tot
    else:
        pro=(0.25)**i + (0.75)**(tot-i)
    prob+=pro

print(1-prob)
