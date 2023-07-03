# №1
# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число. Обрабатывайте не числовые данные как исключения.

def num_exc():
    while True:
        try:
            num = input('Введите целое или вещественное число: ')
            if float(num):
                print('Это правильный ввод)')
            break
        except ValueError as e:
            print(f'Введено не правильное значение: {e}\n Введите другое значение: ')

if __name__ == '__main__':
    num_exc()