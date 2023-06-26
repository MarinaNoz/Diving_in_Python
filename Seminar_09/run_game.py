
if __name__ == '__main__':
    print((f'Выберите игру: \n'
           '1: Конфеты \n'
           '2: Шахматы \n'
           '3: Угадай число'))
    game = int(input('Что выбираем? '))
    if game == 1:
        import candies
        candies()
    if game == 2:
        import chess
        chess()
    if game == 3:
        import check_nums
        check_nums
    else:
        print('А эта игра еще в разработке ))')