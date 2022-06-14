aa=input('insert string\n')

def coun(st):
    a=st.count('A')
    t=st.count('T')
    c=st.count('C')
    g=st.count('G')
    if a==t and c==g:
        return 1
    else:
        return 0


ii='AT'
print(ii.count('G'))
