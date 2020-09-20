k = 0
j = 0
with open('sample.txt') as file:
    d = dict()
    for line in file.readlines():
        if line.find(' ->. ') != -1:
            d[k] = line.rstrip().split(' ->. ')
            d[k].append('stop')
        else:
            d[k] = line.rstrip().split(' -> ')
            d[k].append('continue')
        k += 1


g = open('intr.txt', 'r')
s = g.readline()


def change(stroka, i):
    s1 = d[i][0]
    num = stroka.find(s1)
    if s1 == '0':
        num = 0
    if num > -1:
        if s1 == '0':
            m = 0
        else:
            m = len(s1)
        sn = stroka + 'e'
        if d[i][1] != '0':
            stroka = sn[0:num] + d[i][1] + sn[num+m:-1]
        else:
            stroka = sn[0:num] + sn[num+m:-1]
    return stroka


def go_on(dictionary, i):
    if dictionary[i][2] == 'stop':
        return False
    else:
        return True


def repeat(stroka, i):
    s1 = d[i][0]
    num = stroka.find(s1)
    if s1 == '0':
        num = 0
    if num != -1:
        return True
    else:
        return False


while j < k:
    while repeat(s, j) is True:
        s = change(s, j)
        if go_on(d, j) is False:
            j = k
            break
        j = 0
    j += 1

print(s)
