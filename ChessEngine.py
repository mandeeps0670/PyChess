from settings import *

inCheck = False

moves = []

player = 1


def Evaluation():
    val_sum = 0
    attack_sum = 0
    for i in range(8):
        for j in range(8):
            val_sum += piecearray[i,j]
            attack_sum += temp_attack_array[i,j]

    return -(-1**player)*(10*attack_sum + val_sum)

# def MakeMove(player):
#
#     for piece in piece_group[player]:
#         pass
#
#     pass

def getallmoves(player):
    for piece in piece_group[player]:
        piece.get_moves(moves)


def DoMove():
    pass

def UndoMove():
    pass


def Search(depth,alpha,beta):
    if depth == 0:
        Evaluation()

    #getallmoves()

    if len(moves) == 0:
        if inCheck == True:
            return -10000
        else:
            return 0

    BestGain = -10000
    for piece in piece_group[player]:
        moves.clear()
        piece.get_moves(moves)
        for move in moves:
            if type(move) == str:
                pass
            else:
                pass

    for move in moves:
        DoMove()
        gain = -Search(depth-1, -beta , -alpha)
        UndoMove()
        if gain >= beta:
            return beta
        alpha = max(alpha,gain)

    return alpha