aa=input('insert RNA\n')

A=aa.count('A')
C=aa.count('C')

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

a1=fact(A)
c1=fact(C)

print(a1*c1)
