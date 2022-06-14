import pandas as pd
import csv

f=open('/mnt/c/python_coding/rosalind_kmp.txt','r')
aa=f.read().split('\n')
a1=''
for i in aa:
    a1+=i

f.close()
bb=[0]*len(a1)
print(len(a1))


def chan(st,ar,n):
    while n>-1:
        n=ar.find(st,n)
        if not n:
            bb[0]=0
            n+=len(st)
        elif n> -1:
            bb[n-1+len(st)]=len(st)
            n+=1



for i in range(len(a1)):
    ar1=a1
    dj=ar1[:1+i]
    chan(dj,a1,0)

res=''



with open('/mnt/c/python_coding/result.txt','w') as file:
    writer=csv.writer(file,delimiter=' ')
    writer.writerow(bb)

    

