def line_number(index1, index2, index3):
    print('' + str(board[index1]) + \
          ' | ' + str(board[index2]) + \
          ' | ' + str(board[index3]) + '')


def line():
    print('---------')


def view_board():
    line_number(0, 1, 2)
    line()
    line_number(3, 4, 5)
    line()
    line_number(6, 7, 8)


def check_value():
    n = input('Введите число от 1 до 9: ')
    while not n.isdigit() or int(n) < 0 or int(n) > 9 or not str(board[int(n) - 1]).isdigit():
        print('Ячейка занята или вы ввели не число')
        n = input('Введите число от 1 до 9: ')
    return int(n)


def horizontal():
    if board[0] == board[1] == board[2] or \
            board[3] == board[4] == board[5] or \
            board[6] == board[7] == board[8]:
        return False  # игра закончена
    return True  # игра продолжается


def vertical():
    if board[0] == board[3] == board[6] or \
            board[1] == board[4] == board[7] or \
            board[2] == board[5] == board[8]:
        return False  # игра закончена
    return True  # игра продолжается


def diagonal():
    if board[0] == board[4] == board[8] or \
       board[2] == board[4] == board[6]:
        return False #игра закончена
    return True #игра продолжается


board = [x + 1 for x in range(10)]
step = 0

while horizontal() and vertical()and diagonal() \
      and step < 9:
    view_board()
    if step % 2 == 0:
        sign = 'X'
    else:
        sign = 'O'
    cell_number = check_value()
    board[cell_number - 1] = sign
    step += 1

view_board()
if step == 9:
    print('Ничья')
else:
    print('Win', sign)