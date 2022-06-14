from math import factorial
aa=input('insert strings\n')
A=aa.count('A')
U=aa.count('U')
C=aa.count('C')
G=aa.count('G')

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)



def perm(c,g):
    if c>g:
        c,g=g,c

    return fact(g)/fact(g-c)

print(int(perm(A,U)*perm(G,C)))

if U>A:
    U,A=A,U
if G>C:
    G,C=C,G

AU = factorial(A)/factorial(A-U)
GC = factorial(C)/factorial(C-G)

print(int(AU*GC))
