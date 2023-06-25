#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_str(absolute_path: str):
    def define(absolute: str, separator: str) -> tuple:
        absolute = absolute.split(separator)
        file_name, expansion = absolute[-1].split('.')
        path = separator.join(absolute[:-1])
        return path, file_name, expansion
    return define(absolute_path, '/')

print(split_str(r'C:/DZ_Python/DZ_Seminar5/task_1.py'))

