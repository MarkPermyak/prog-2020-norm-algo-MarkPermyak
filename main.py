k = 0
with open('sample.txt') as file:
    d = dict()
    for line in file.readlines():
        if line.find(' ->. ') != -1:
            d[k] = line.rstrip().split(' ->. ')
        else:
            d[k] = line.rstrip().split(' -> ')
        k += 1

g = open('intr.txt', 'r')
s = g.readline()


def change(s, i):
    s1 = d[i][0]
    num = s.find(s1)
    if s1 == '0':
        num = 0
    if num > -1:
        if s1 == '0':
            l = 0
        else:
            l = len(s1)
        sn = s + 'e'
        if d[i][1] != '0':
            s = sn[0:num] + d[i][1] + sn[num+l:-1]
        else:

                s = sn[0:num] + sn[num+l:-1]

    return s


for j in range(0, k):
    s = change(s, j)

print(s)
