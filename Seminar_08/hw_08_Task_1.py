# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle. - Для дочерних объектов указывайте родительскую директорию. 
#- Для каждого объекта укажите файл это или директория. 
#- Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import json
import csv
import pickle
import os


def write_json(data: dict, path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name + '.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def write_csv(data: dict, path_: str, file_: str) -> None:
    file_path = os.path.join(path_, file_ + '.csv')
    new_data = [['path: ', 'type: ',  'name: ', 'size: ', 'dir: ', ]]
    for i, j in data.items():
        new_data.append([i, *j.values()])
    with open(file_path, 'w', encoding='utf-8') as f:
        write_csv = csv.writer(f, dialect='excel', delimiter=';')
        write_csv.writerows(data)


def write_pickle(data: dict, path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name + '.bin')
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)


def file_inf(data: dict[str, dict[str]],
                  path: str,
                  name: str,
                  type: str) -> None:
    if type == 'File':
        data[path] = dict(type_='File',
                               name_=name,
                               size_=os.path.getsize(os.path.join(path, name)),
                               dir_=os.path.split(path)[-1])
    elif type == 'D':
        data[path] = dict(type_='Dir',
                               name_=name,
                               size_=count_size(os.path.join(path, name)),
                               dir_=os.path.split(os.path.abspath(path))[-1])


def count_size(count_path: str, dir_size: int = 0) -> float:
    for sub_item in os.walk(count_path):
        if sub_item[2]:
            dir_size += sum([os.path.getsize(os.path.join(sub_item[0], file))
                             for file in sub_item[2]])
        if sub_item[1]:
            dir_size += sum([count_size(os.path.join(sub_item[0], subdir))
                             for subdir in sub_item[1]])
    return dir_size


def dir_info(data: str, dict_: dict = None) -> dict[str, dict[str]]:
    if dict_ is None:
        dict_ = {}
        path_ = os.path.split(os.path.abspath(data))
        file_inf(dict_, os.path.join(*path_[:-1]), path_[-1], 'Dir')

    for item in os.listdir(data):
        check_path = os.path.join(data, item)
        if os.path.isfile(check_path):
            file_inf(dict_, data, item, 'File')
        elif os.path.isdir(check_path):
            file_inf(dict_, data, item, 'Dir')
            dir_info(os.path.join(data, item), dict_)
    return dict_


def dict_printer(in_dict: dict) -> None:
    for i, j in sorted(in_dict.items()):
        print(i, end=':')
        if isinstance(j, dict):
            print()
            dict_printer(j)
        else:
            print('\t', j)


def main():
    path_ = 'c:\\1\\DivingInPython\\DivingInPython\\seminar_8\\'
    result = dir_info(path_)
    write_json(result, os.getcwd(), 'result')
    write_pickle(result, os.getcwd(), 'result')
    write_csv(result, os.getcwd(), 'result')


if __name__ == '__main__':
    main()
