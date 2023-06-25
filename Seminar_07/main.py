from feel_numbers import feel_numbers
from name_gen import name_gen
from two_files_in_one import two_files_in_one
from gen_files import gen_files
from hw_07_Task_1 import file_rename


if __name__ == '__main__':
    feel_numbers(3, 'file1.txt')
    name_gen(10, 4, 7, 'file_2.txt')
    two_files_in_one('file_1.txt', 'file_2.txt', 'result.txt')
    gen_files('bin', 5, 10, 1204, 4096, 5)
    file_rename()