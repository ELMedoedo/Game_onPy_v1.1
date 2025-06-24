import random


def print_board(board):  # Вывод поля

    print("  1 2 3")
    for i in range(len(board)):
        print(chr(65 + i), end=" ")
        print(*board[i], sep="|")
        if i < 2:
            print("  ------")


def check_winner(board):
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != ".":
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ".":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ".":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ".":
        return board[0][2]

    
    if all(cel != "." for row in board for cel in row):    # Проверка на ничью
        return "Dr"

    return None


def computer_move(board, computer_symbol):
    # Ход компьютера

    for i in range(3):  # Проверка на возможность победы компьютера
        for j in range(3):
            if board[i][j] == ".":
                board[i][j] = computer_symbol
                if check_winner(board) == computer_symbol:
                    return (i, j)
                board[i][j] = "."

    player_symbol = (
        "X" if computer_symbol == "O" else "O"
    )  # проверка на выйгрыш игнрока
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                board[i][j] = player_symbol
                if check_winner(board) == player_symbol:
                    board[i][j] = computer_symbol
                    return (i, j)
                board[i][j] = "."

    if board[1][1] == ".":  # Если центр свободен, занимаем его
        return (1, 1)

    empty_cells = []  # Иначе случайный ход
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                empty_cells.append((i, j))

    return random.choice(empty_cells)


def play_game():  # основа
    while True:
        
        player_symbol = input("Выберите чем играть (X или O): ").upper()    # Выбор символа
        while player_symbol not in ["X", "O"]:
            player_symbol = input("Пожалуйста, выберите X или O: ").upper()

        computer_symbol = "O" if player_symbol == "X" else "X"

        board = [
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
        ]  # Инициализация доски

        turn = (
            "player" if player_symbol == "X" else "computer"
        )  # Определение очередности хода

        print("Начинаем игру!")
        print_board(board)

        while True:
            if turn == "player":  # Ход игрока
                while True:
                    move = input("Ваш ход (например A1, B2, C3): ").upper()
                    if (
                        len(move) == 2
                        and move[0] in ["A", "B", "C"]
                        and move[1] in ["1", "2", "3"]
                    ):
                        row = ord(move[0]) - ord("A")
                        col = int(move[1]) - 1
                        if board[row][col] == ".":
                            board[row][col] = player_symbol
                            break
                        else:
                            print("Эта клетка уже занята!")
                    else:
                        print("Некорректный ввод. Попробуйте еще раз.")

                turn = "computer"
            else:
                print("Ход компьютера...")  # Ход компьютера
                row, col = computer_move(board, computer_symbol)
                board[row][col] = computer_symbol
                turn = "player"

            print_board(board)

            result = check_winner(board)  # Проверка на победу или ничью
            if result == player_symbol:
                print("Поздравляю! Вы победили!")
                break
            elif result == computer_symbol:
                print("Компьютер победил!")
                break
            elif result == "Dr":
                print("Ничья!")
                break

        play_again = input("Хотите сыграть еще раз? (y/n): ").lower()
        while play_again not in ["y", "n"]:
            play_again = input("Пожалуйста, введите 'y' или 'n': ").lower()

        if play_again == "n":
            print("Спасибо за игру! До свидания!")
            break

play_game()   
