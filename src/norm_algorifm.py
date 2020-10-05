number_of_substitutions = 0


with open('../data/scheme.txt') as file:
    for line in file.readlines():
        number_of_substitutions += 1


current_string = 0
list_of_substitutions = list(range(number_of_substitutions))

with open('../data/scheme.txt') as file:
    for line in file.readlines():
        if line.find(' ->. ') != -1:
            list_of_substitutions[current_string] = line.rstrip().split(' ->. ')
            list_of_substitutions[current_string].append('stop')
        else:
            list_of_substitutions[current_string] = line.rstrip().split(' -> ')
            list_of_substitutions[current_string].append('continue')
        current_string += 1
# заполняем словарик, ключами которого являются числа от 0 до k-1, а значениями списки из трёх элементов: левая часть
# подстановки, правая часть подстановки и значение stop или continue для завершающей и незавершающей подстановки
# соответсвенно

result_file = open('../src/result.txt', 'w')
initial_file = open('../data/introductory_string.txt', 'r')
initial_string = initial_file.readline()
new_string = initial_string


def change(string, i):
    s1 = list_of_substitutions[i][0]
    num = string.find(s1)
    if s1 == '0':
        # если левая часть подстановки - пустое слово
        num = 0
    if num > -1:
        # если подстрока нашлась
        if s1 == '0':
            m = 0
        else:
            m = len(s1)
        sn = string + 'e'
        # добавим в конец символ (который вскоре все равно обрежется) для корректной работы функции
        if list_of_substitutions[i][1] != '0':
            string = sn[0:num] + list_of_substitutions[i][1] + sn[num+m:-1]
            # вырезаем левую часть подстановки и заменяем правой
        else:
            string = sn[0:num] + sn[num+m:-1]
            # просто вырезаем левую часть подстановки
    return string


def is_substitution_final(dictionary, i):
    if dictionary[i][2] == 'stop':
        # проверка на незаключительность
        return True
    else:
        return False


def repeat(string, i):
    s1 = list_of_substitutions[i][0]
    num = string.find(s1)
    if s1 == '0':
        num = 0
    if num != -1:
        # проверка нахождения левой части подстановки в строчке
        return True
    else:
        return False


j = 0
while j < number_of_substitutions:
    # пока не дойдем до конца схемы
    while repeat(new_string, j) is True:
        # делать подстановку пока делается (если не завершающая)
        new_string = change(new_string, j)
        if is_substitution_final(list_of_substitutions, j) is True:
            j = number_of_substitutions
            break
            # если подстановка оказалась завершающей, закончить весь цикл после первого выполнения
        j = 0
        # начать схему заново, чтоб не пропустить более приоритетные подстановки
    j += 1
    # если все подстановки до этого выполнены, спускаемся ниже

print(number_of_substitutions)
result_file.write(new_string)
