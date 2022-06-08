f=open('/mnt/c/python_coding/aa.txt','r')
aa=f.read().split('\n')
ros=list()
ros=aa[::3]
ros2=list()
seq1=aa[1::3]
seq2=aa[2::3]
#they give file with like >ros \n AGCCCT \n AGGT
for i in ros:
        i2=i.strip(">")
        ros2.append(i2)


f.close()

f=open('/mnt/c/python_coding/result.txt','w')

for i in range(len(ros2)):
    o3=seq2[i][len(seq2[i])-3:len(seq2[i])]
    for j in range(len(ros2)):
        o32=seq1[j][0:3]
        if o3==o32 and i!=j:
            f.write('%s %s\n' % (ros2[i],ros2[j]))


        


