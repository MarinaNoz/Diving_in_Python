# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.
import string


def remove_chars(text: str) -> str:
    alpha = string.ascii_letters + ' '
    print(alpha)
    result = text
    for t in text:
        if t not in alpha:
            result = result.replace(t, '')
    return result.lower()


if __name__ == '__main__':
    print(remove_chars('addSDGdsafsdfsd aghавпыпFSDHряывап 23552#%13'))