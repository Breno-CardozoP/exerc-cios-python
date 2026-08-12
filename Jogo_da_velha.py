import random

board=[]
contador=1
for i in range(3):
    row=[]
    for j in range(3):
        row.append(contador)
        contador+=1
    board.append(row)

def display(board):
    for row in board:
        print(row)

def enter_move(board):
    display(board)
    posição=int(input(("escolha a posição para jogar: ")))
    return posição

def make_move(board):
    posição=enter_move(board)
    for i in range(3):
        for j in range(3):
            if posição == board[i][j]:
                board[i][j]="X"
                return

def freeBoard(board):
    free=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ('X', 'O'):
                free.append((i,j))
    return free

def PC_move(board):
    vazio = freeBoard(board)
    linha,coluna = random.choice(vazio)
    board[linha][coluna] = 'O'
    return linha,coluna

def check_winner(board, jogador):
    
    for i in range(3):
        if board[i][0] == jogador and board[i][1] == jogador and board[i][2] == jogador:
            return True

    for j in range(3):
        if board[0][j] == jogador and board[1][j] == jogador and board[2][j] == jogador:
            return True

    if board[0][0] == jogador and board[1][1] == jogador and board[2][2] == jogador:
        return True

    if board[0][2] == jogador and board[1][1] == jogador and board[2][0] == jogador:
        return True

    return False


def winner(board):
    while True:
        make_move(board)
        display(board)

        if check_winner(board, 'X'):
            print("O jogador ganhou.")
            break

        if not freeBoard(board):
            print("Empate!")
            break

        PC_move(board)
        display(board)

        if check_winner(board, 'O'):
            print("O computador ganhou.")
            break

        if not freeBoard(board):
            print("Empate!")
            break

winner(board)
        

            



    










