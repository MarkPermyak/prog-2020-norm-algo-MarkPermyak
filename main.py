k=0
with open('sample.txt') as file:
    d = dict()
    for line in file.readlines():
        d[k]=line.rstrip().split(' -> ');
        k+=1

g=open('intr.txt','r')
s=g.readline()

def change(s,i):
    s1=d[i][0]
    num=s.find(s1)
    if (num>-1):
        l = len(s1)
        sn = s + 'e'
        s = sn[0:num] + d[i][1] + sn[num+l:-1]
    return(s)
for j in range (0,k):
    s=change(s,j)