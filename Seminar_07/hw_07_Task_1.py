# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def file_rename(path, new_name, digit_light, extention4rename, new_extention, old_name):

    path = path
    new_name = new_name
    digit_light = digit_light
    extention4rename = extention4rename
    new_extension = new_extention
    remainder_name = old_name
    max_len_zero = '0000000000'
    extention_list = [i for i in path][0][2]
    find_files = [i for i in extention_list if i.split('.')[1] == extention4rename]
    name4rename_begin = remainder_name[0]
    name4rename_end = remainder_name[1]
    name_old_files = [i.split('.')[0][name4rename_begin:name4rename_end] for i in find_files]
    name_new_files = [i + '_' + new_name + '.' + new_extension for i in name_old_files]
    new_digit_part = max_len_zero[:digit_light]
    name_new_files_list = []

    for i in enumerate(name_new_files):
        name_new_files_list.append(
            i[1].split('.')[0] + '_' + str(new_digit_part[:-len(str(i[0]))]) + str(i[0]) + '.' + i[1].split('.')[1])

    return find_files, name_new_files_list

path_file = input('Введите путь к папке (в формате c:\\1\DivingInPython\\): ')
path_name = os.walk(path_file)
new_name = input('Введите добавляемое имя файла: ')
digit_light = int(input('Введите колличество цифр для добавления к имени файла: '))
extention4rename = input('Введите расширение файла которое необходимо переименовать: ')
new_extension = input('Введите расширение файла в которое будет переименовано: ')
a = int(input('Введите начальный номер символа cвреза имени файла который необходимо оставить: '))
b = int(input('Введите конечный номер символа cвреза имени файла который необходимо оставить: '))
remainder_name = [a, b]
list_names = file_rename(path_name, new_name, digit_light, extention4rename, new_extension, remainder_name)

for i in range(len(list_names[0])):
    os.rename(path_file + '\\' +  list_names[0][i], path_file + '\\' + list_names[1][i])