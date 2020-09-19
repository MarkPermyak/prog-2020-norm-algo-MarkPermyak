k=0
with open('sample.txt') as file:
    d = dict()
    for line in file.readlines():
        d[k]=line.rstrip().split(' -> ');
        k+=1

