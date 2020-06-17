import random
import time

def getPos(a):
    while True:
        try:
            number = int(input("Enter position (1-9): "))
            if 1 <= number < 10:
                if a[number - 1] == 'X' or a[number - 1] == 'O':
                    print("Slot already used! Try Again!")
                    continue
                else:
                    return number - 1
            else:
                print("Please enter a number from 1 to 9 only!")
                continue
        except ValueError:
            print("Please only enter a number!")
            continue


def getOption():
    while True:
        try:
            i = int(input('1. Two Player\n2. One Player\n3. Exit\n\nEnter Option: '))
            if 1 <= i < 4:
                return i
            else:
                print("Please enter a number from 1 to 4 only!")
                continue
        except ValueError:
            print("Please only enter a number!")
            continue


def printBoard(b):
    print('\n')
    print(b[0] + ' | ' + b[1] + ' | ' + b[2])
    print('----------')
    print(b[3] + ' | ' + b[4] + ' | ' + b[5])
    print('----------')
    print(b[6] + ' | ' + b[7] + ' | ' + b[8])


def isWinner(b, current_player):
    won: bool
    if (b[0] == current_player and b[4] == current_player and b[8] == current_player) or (
            (b[2] == current_player and b[4] == current_player and b[6] == current_player)):
        won = True
        return won

    for posx in range(0, 3):
        posy = posx * 3
        if b[posy] == current_player and b[(posy + 1)] == current_player and b[(posy + 2)] == current_player:
            won = True
            return won
        if b[posx] == current_player and b[(posx + 3)] == current_player and b[(posx + 6)] == current_player:
            won = True
            return won


def makeMove(board, current_player, move):
    board[move] = current_player


def boardCopy(board):
    cloneBoard = []
    for pos in board:
        cloneBoard.append(pos)
    return cloneBoard


def isSpaceAvailable(board, move):
    return board[move] != 'X' and board[move] != 'O'


def getRandomMove(board, moves):
    availableMoves = []
    for move in moves:
        if isSpaceAvailable(board, move):
            availableMoves.append(move)

    if availableMoves.__len__() != 0:
        return random.choice(availableMoves)
    else:
        return None


def makeComputerMove(board, computerPlayer):
    if computerPlayer == 'X':
        humanPlayer = 'O'
    else:
        humanPlayer = 'X'

    for pos in range(0, 9):
        clone = boardCopy(board)
        if isSpaceAvailable(clone, pos):
            makeMove(clone, computerPlayer, pos)
            if isWinner(clone, computerPlayer):
                return pos

    for pos in range(0, 9):
        clone = boardCopy(board)
        if isSpaceAvailable(clone, pos):
            makeMove(clone, humanPlayer, pos)
            if isWinner(clone, humanPlayer):
                return pos

    if isSpaceAvailable(board, 5):
        return 5

    move = getRandomMove(board, [1, 3, 7, 9])
    if move is not None:
        return move

    return getRandomMove(board, [2, 4, 6, 8])


def game():
    while True:
        choices = [' '] * 9
        player, computer = 'X', 'O'
        turn = "human"
        player_one = True
        i = getOption()
        if i == 1:
            printBoard(choices)
            while True:
                if player_one:
                    print("\nPlayer X")
                else:
                    print("\nPlayer O")
                player1, player2 = 'X', 'O'
                pos = getPos(choices)
                if player_one:
                    choices[pos] = "X"
                else:
                    choices[pos] = "O"
                full = True
                for x in range(0, 9):
                    if choices[x] != 'X' and choices[x] != "O":
                        full = False
                if player_one:
                    if isWinner(choices, player1):
                        printBoard(choices)
                        print("Player 1 won the game!\n")
                        time.sleep(3)
                        game()

                    else:
                        printBoard(choices)
                        player_one = not player_one

                elif not player_one:
                    if isWinner(choices, player2):
                        printBoard(choices)
                        print("Player 2 won the game!\n")
                        time.sleep(3)
                        game()
                    else:
                        printBoard(choices)
                        player_one = not player_one

                if full:
                    print("It's a tie!\n")
                    time.sleep(3)
                    game()

        elif i == 2:
            print("\nThe " + turn + " will start the game\n")
            while True:
                full = True
                for x in range(0, 9):
                    if choices[x] != 'X' and choices[x] != "O":
                        full = False
                if full:
                    print("\nIt's a tie!\n")
                    time.sleep(3)
                    game()
                elif turn == "human":
                    printBoard(choices)
                    move = getPos(choices)
                    makeMove(choices, player, move)
                    if isWinner(choices, player):
                        printBoard(choices)
                        print("\nYou won the game!\n")
                        time.sleep(3)
                        game()
                    else:
                        printBoard(choices)
                        turn = 'computer'
                else:
                    move = makeComputerMove(choices, computer)
                    makeMove(choices, computer, move)
                    if isWinner(choices, computer):
                        printBoard(choices)
                        print('\nYou loose!\n')
                        time.sleep(3)
                        game()
                    else:
                        turn = 'human'

        elif i == 3:
            exit()

if __name__ == '__main__':
    game()