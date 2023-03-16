from random import randint


def easy_bot(candies, max_cand):
    move = randint(1, max_cand) if candies >= max_cand else randint(1, candies)
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies


def hard_bot(candies, max_cand):
    move = candies % (max_cand + 1)
    if move == 0:
        move = randint(1, max_cand) if candies >= max_cand else candies
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies


def check_win(candies, determing_moves, first_name, second_name):
    if candies == 0:
        return first_name if determing_moves % 2 == 0 else second_name
    else:
        return False


def player_vs_easy_bot():
    name_player = input('Введите свое имя: ')
    candies = 2021
    max_cand = 28
    count_for_check_win = candies // max_cand
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = move_player(name_player, candies, max_cand)
        else:
            candies = easy_bot(candies, max_cand)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(candies, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1


def player_vs_hard_bot():
    name_player = input('Введите свое имя: ')
    candies = 2021
    max_cand = 28
    count_for_check_win = candies // max_cand
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = move_player(name_player, candies, max_cand)
        else:
            candies = hard_bot(candies, max_cand)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(candies, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1


def player_vs_player():
    name_first_player = input('Введите имя первого игрока: ')
    name_second_player = input('Введите имя второго игрока: ')
    candies = input('Введите количество конфет: ')
    max_cand = 28
    count_for_check_win = candies // max_cand
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = move_player(name_first_player, candies, max_cand)
        else:
            candies = move_player(name_second_player, candies, max_cand)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(candies, determing_moves,
                             name_first_player, name_second_player)
            if temp:
                print(f'{temp} выиграл(а)')
                win = True
        determing_moves += 1


def move_player(name_player, candies, max_cand):
    valid = False
    while not valid:
        move = input(f'{name_player}, Ваш ход... ')
        try:
            move = int(move)
            if move > 0 and move <= max_cand and move <= candies:
                print(f'Вы забрали {move} конфет')
                candies -= move
                print(f'Осталось {candies} конфет')
                valid = True
            else:
                print(
                    f'Количество взятых конфет должно быть в интервале от 1 до {max_cand} или не больше оставшегося количества конфет')
        except:
            print('Необходимо ввести целое число.')
    return candies


type_game = input(
    'Введите 1, если хотите играть с другим игроком, и любую другую цифру, если с ботом... ')
if (type_game == '1'):
    player_vs_player()
else:
    intel = input(
        'Введите 0, если хотите играть с глупым ботом, и любую другую цифру, если с умным... ')
    if intel == '0':
        player_vs_easy_bot()
    else:
        player_vs_hard_bot()
