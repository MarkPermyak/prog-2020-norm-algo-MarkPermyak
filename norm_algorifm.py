k = 0


with open('scheme.txt') as file:
    d = dict()
    for line in file.readlines():
        if line.find(' ->. ') != -1:
            d[k] = line.rstrip().split(' ->. ')
            d[k].append('stop')
        else:
            d[k] = line.rstrip().split(' -> ')
            d[k].append('continue')
        k += 1
# заполняем словарик, ключами которого являются числа от 0 до k-1, а значениями списки из трёх элементов: левая часть
# подстановки, правая часть подстановки и значение stop или continue для завершающей и незавершающей подстановки
# соответсвенно

t = open('result.txt', 'w')
g = open('introductory_string.txt', 'r')
s = g.readline()


def change(stroka, i):
    s1 = d[i][0]
    num = stroka.find(s1)
    if s1 == '0':
        # если левая часть подстановки - пустое слово
        num = 0
    if num > -1:
        # если подстрока нашлась
        if s1 == '0':
            m = 0
        else:
            m = len(s1)
        sn = stroka + 'e'
        # добавим в конец символ (который вскоре все равно обрежется) для корректной работы функции
        if d[i][1] != '0':
            stroka = sn[0:num] + d[i][1] + sn[num+m:-1]
            # вырезаем левую часть подстановки и заменяем правой
        else:
            stroka = sn[0:num] + sn[num+m:-1]
            # просто вырезаем левую часть подстановки
    return stroka


def go_on(dictionary, i):
    if dictionary[i][2] == 'stop':
        # проверка на незаключительность
        return False
    else:
        return True


def repeat(stroka, i):
    s1 = d[i][0]
    num = stroka.find(s1)
    if s1 == '0':
        num = 0
    if num != -1:
        # проверка нахождения левой части подстановки в строчке
        return True
    else:
        return False


j = 0
while j < k:
    # пока не дойдем до конца схемы
    while repeat(s, j) is True:
        # делать подстановку пока делается (если не завершающая)
        s = change(s, j)
        if go_on(d, j) is False:
            j = k
            break
            # если подстановка оказалась завершающей, закончить весь цикл после первого выполнения
        j = 0
        # начать схему заново, чтоб не пропустить более приоритетные подстановки
    j += 1
    # если все подстановки до этого выполнены, спускаемся ниже


t.write(s)
