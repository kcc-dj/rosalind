a1=input('first\n')
a2=input('second\n')

n=0
for i in range(len(a1)):
    if a1[i]!=a2[i]:
        n+=1

print(n)

