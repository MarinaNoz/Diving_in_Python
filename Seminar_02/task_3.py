# Напишите программу, которая получает целое число и возвращает
#его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
#результата, а не для решения
#Попробуйте избежать дублирования кода
#в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно


def task3(num: int, mode: str) -> str:
    result = ''
    convert: int = 2
    match mode:
        case 'bin':
            convert = 2
        case "oct":
            convert = 8
    while num >= 1:
        res = num % convert
        result += str(res)
        num = num // convert

    return result[::-1]

print(task3(21, mode="bin"), f"assert: {bin(21)}")
print(task3(21, mode="oct"), f'assert: {oct(21)}')
