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


def replace_substring(string, num_substring):
    replaced_substring = list_of_substitutions[num_substring][0]
    ind = string.find(replaced_substring)
    if replaced_substring == '0':
        # если левая часть подстановки - пустое слово
        ind = 0
    if ind > -1:
        # если подстрока нашлась
        if replaced_substring == '0':
            len_of_replaced_substring = 0
        else:
            len_of_replaced_substring = len(replaced_substring)
        string = string + 'e'
        # добавим в конец символ (который вскоре все равно обрежется) для корректной работы функции
        if list_of_substitutions[num_substring][1] != '0':
            string = string[0:ind] + list_of_substitutions[num_substring][1] + string[ind+len_of_replaced_substring:-1]
            # вырезаем левую часть подстановки и заменяем правой
        else:
            string = string[0:ind] + string[ind+len_of_replaced_substring:-1]
            # просто вырезаем левую часть подстановки
    return string


def is_substitution_final(list_of_string, number_of_substring):
    if list_of_string[number_of_substring][2] == 'stop':
        # проверка на незаключительность
        return True
    else:
        return False


def repeat(string, number_of_substring):
    replaced_substring = list_of_substitutions[number_of_substring][0]
    ind = string.find(replaced_substring)
    if replaced_substring == '0':
        ind = 0
    if ind != -1:
        # проверка нахождения левой части подстановки в строчке
        return True
    else:
        return False


def make_a_substitute(string):
    global current_string
    while repeat(string, current_string) is True:
        # делать подстановку пока делается (если не завершающая)
        string = replace_substring(string, current_string)
        if is_substitution_final(list_of_substitutions, current_string) is True:
            current_string = number_of_substitutions
            break
            # если подстановка оказалась завершающей, закончить весь цикл после первого выполнения
        current_string = 0
        # начать схему заново, чтоб не пропустить более приоритетные подстановки
    return string


current_string = 0
while current_string < number_of_substitutions:
    # пока не дойдем до конца схемы
    new_string = make_a_substitute(new_string)
    current_string += 1

    # если все подстановки до этого выполнены, спускаемся ниже

result_file.write(new_string)
