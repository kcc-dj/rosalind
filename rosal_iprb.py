aa=input('insert k,m,n\n')

aa=aa.split()
k=int(aa[0])
m=int(aa[1])
n=int(aa[2])

tot=k+m+n

n1=n*(n-1)*0.5
mn=m*n*0.5
m1=m*(m-1)*0.25*0.5

totn=tot*(tot-1)*0.5
print((totn-n1-mn-m1)/totn)
