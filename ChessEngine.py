import numpy as np

from ChessPiece import inbrd, makepseudomove, attackCalc
from settings import *

inCheck = False

moves = []

BestGain = -10000

BestMove = None

Depth_Searched = 7


def Evaluation(player):
    val_sum = 0
    attack_sum = 0
    for i in range(8):
        for j in range(8):
            if piecearray[i,j] != 0:
                if piecearray[i,j] > 0:
                    c = j
                else:
                    c = 7-j

                if abs(piecearray[i,j]) == 100:
                    val_sum += piecearray[i, j] + PawnTable[i,c]
                elif abs(piecearray[i,j]) == 300:
                    val_sum += piecearray[i, j] + BishopTable[i, c]
                elif abs(piecearray[i,j]) == 302:
                    val_sum += piecearray[i, j] + KnightTable[i, c]
                elif abs(piecearray[i,j] )== 500 or abs(piecearray[i,c]) == 501:
                    val_sum += piecearray[i, j] + RookTable[i, c]
                elif abs(piecearray[i,j] )== 900:
                    val_sum += piecearray[i, j] + QueenTable[i, c]
                elif abs(piecearray[i,j] )== 1000 or abs(piecearray[i,j] )== 1001:
                    val_sum += piecearray[i, j] + KingTable[i, c]
            attack_sum += temp_attack_array[i, j]

    return (-1 ** player) * (10 * attack_sum + val_sum)


# def MakeMove(player):
#
#     for piece in piece_group[player]:
#         pass
#
#     pass


def DoMove():
    pass


def UndoMove():
    pass


def CastleMove(move):
    if move[1] == 'Q':
        piecearray[0, 0] = 0
        piecearray[4, 0] = 0
        piecearray[2, 0] = 1000
        piecearray[3, 0] = 500
    elif move[1] == 'q':
        piecearray[0, 7] = 0
        piecearray[4, 7] = 0
        piecearray[2, 7] = -1000
        piecearray[3, 7] = -500
    elif move[1] == 'K':
        piecearray[7, 0] = 0
        piecearray[4, 0] = 0
        piecearray[6, 0] = 1000
        piecearray[5, 0] = 500
    elif move[1] == 'k':
        piecearray[7, 7] = 0
        piecearray[4, 7] = 0
        piecearray[6, 7] = -1000
        piecearray[5, 7] = -500


def UndoCastleMove(move):
    if move[1] == 'Q':
        piecearray[0, 0] = 501
        piecearray[4, 0] = 1001
        piecearray[2, 0] = 0
        piecearray[3, 0] = 0
    elif move[1] == 'q':
        piecearray[0, 7] = -501
        piecearray[4, 7] = -1001
        piecearray[2, 7] = 0
        piecearray[3, 7] = 0
    elif move[1] == 'K':
        piecearray[7, 0] = 501
        piecearray[4, 0] = 1001
        piecearray[6, 0] = 0
        piecearray[5, 0] = 0
    elif move[1] == 'k':
        piecearray[7, 7] = -501
        piecearray[4, 7] = -1001
        piecearray[6, 7] = 0
        piecearray[5, 7] = 0


def do_undo(locn_old, locn_new, depth, alpha, beta, player):
    pieceval = piecearray[tuple(locn_old)]
    attackval = piecearray[tuple(locn_new)]
    piecearray[tuple(locn_old)] = 0
    piecearray[tuple(locn_new)] = pieceval
    player += 1
    # Compute
    gain = -Search(depth - 1, -beta, -alpha, player)
    player -= 1
    # UndoMove
    piecearray[tuple(locn_old)] = pieceval
    piecearray[tuple(locn_new)] = attackval

    return gain


def comp(locn_old, locn_new):
    val_old = 8 * locn_old[0] + locn_old[1]
    val_new = 8 * locn_new[0] + locn_new[1]

    return 100 * val_new + val_old


def CanCastle(value):
    if value == 1001 or value == 501:
        temp_attack_array.fill(0)
        for piece in piece_group[1]:
            attackCalc(temp_attack_array, piece.location)
        # print(temp_attack_array)
        if piecearray[4, 0] == 1001:
            # if self.location == np.array([0,0]) or self.location == np.array([0,0]):
            ##print("K")
            if piecearray[0, 0] == 501:
                if piecearray[2, 0] == 0 and piecearray[3, 0] == 0:
                    if temp_attack_array[2, 0] == 0 and temp_attack_array[3, 0] == 0 and temp_attack_array[4, 0] == 0:
                        return 'Q'
            # if self.location == np.array([7, 0]):
            if piecearray[7, 0] == 501:
                if piecearray[5, 0] == 0 and piecearray[6, 0] == 0:
                    if temp_attack_array[6, 0] == 0 and temp_attack_array[5, 0] == 0 and temp_attack_array[4, 0] == 0:
                        return 'K'
    elif value == -1001 or value == -501:
        temp_attack_array.fill(0)
        for piece in piece_group[0]:
            attackCalc(temp_attack_array, piece.location)

        if piecearray[4, 7] == -1001:
            if piecearray[0, 7] == -501:
                if piecearray[2, 7] == 0 and piecearray[3, 7] == 0:
                    if temp_attack_array[2, 7] == 0 and temp_attack_array[3, 7] == 0 and temp_attack_array[4, 7] == 0:
                        return 'q'

            if piecearray[7, 7] == -501:
                if piecearray[5, 7] == 0 and piecearray[6, 7] == 0:
                    if temp_attack_array[6, 7] == 0 and temp_attack_array[5, 7] == 0 and temp_attack_array[4, 7] == 0:
                        return 'k'

    else:
        return False


def getallmoves(value, locn, arr):
    if value == 100:
        move = np.array([0, 1])
        if inbrd(locn + move) and piecearray[tuple(locn + move)] == 0:
            if makepseudomove(locn, locn + move):
                arr.append(comp(locn, locn + move))
        if locn[1] == 1 and piecearray[tuple(locn + 2 * move)] == 0 and piecearray[tuple(locn + move)] == 0:
            if makepseudomove(locn, locn + 2 * move):
                arr.append(comp(locn, locn + 2 * move))
        move = np.array([1, 1])
        if inbrd(locn + move) and piecearray[tuple(locn + move)] < 0:
            if makepseudomove(locn, locn + move):
                arr.append(comp(locn, locn + move))
        move = np.array([-1, 1])
        if inbrd(locn + move) and piecearray[tuple(locn + move)] < 0:
            if makepseudomove(locn, locn + move):
                arr.append(comp(locn, locn + move))
    elif value == -100:
        move = np.array([0, -1])
        if inbrd(locn + move) and piecearray[tuple(locn + move)] == 0:
            if makepseudomove(locn, locn + move):
                arr.append(comp(locn, locn + move))

        if locn[1] == 6 and piecearray[tuple(locn + 2 * move)] == 0 and piecearray[tuple(locn + move)] == 0:
            if makepseudomove(locn, locn + 2 * move):
                arr.append(comp(locn, locn + 2 * move))
        move = np.array([1, -1])
        if inbrd(locn + move) and piecearray[tuple(locn + move)] > 0:
            if makepseudomove(locn, locn + move):
                arr.append(comp(locn, locn + move))
        move = np.array([-1, -1])
        if inbrd(locn + move) and piecearray[tuple(locn + move)] > 0:
            if makepseudomove(locn, locn + move):
                arr.append(comp(locn, locn + move))



    elif value == 302 or value == -302:
        moves = np.array([
            [2, 1], [-2, 1], [-2, -1], [2, -1], [
                1, 2], [-1, 2], [-1, -2], [1, -2]])
        for move in moves:
            if inbrd(locn + move) and piecearray[tuple(locn + move)] * np.sign(value) <= 0:
                if makepseudomove(locn, locn + move):
                    arr.append(comp(locn, locn + move))

    elif value == 300 or value == -300:
        moves = np.array([
            [1, 1], [-1, 1], [-1, -1], [1, -1]])
        for move in moves:
            for k in range(1, 8):

                if inbrd(locn + k * move) and piecearray[tuple(locn + k * move)] == 0:
                    if makepseudomove(locn, locn + k * move):
                        arr.append(comp(locn, locn + k * move))
                elif inbrd(locn + k * move) and piecearray[tuple(locn + k * move)] * np.sign(value) < 0:
                    if makepseudomove(locn, locn + k * move):
                        arr.append(comp(locn, locn + k * move))
                    break
                else:
                    break
                # elif inbrd(locn + k*move) and piecearray[tuple(locn + k*move)] * value > 0:
                #     break
    elif value == 500 or value == -500 or value == 501 or value == -501:
        moves = np.array([
            [1, 0], [-1, 0], [0, -1], [0, 1]])
        for move in moves:
            for k in range(1, 8):
                if inbrd(locn + k * move) and piecearray[tuple(locn + k * move)] == 0:
                    if makepseudomove(locn, locn + k * move):
                        arr.append(comp(locn, locn + k * move))
                elif inbrd(locn + k * move) and piecearray[tuple(locn + k * move)] * np.sign(value) < 0:
                    if makepseudomove(locn, locn + k * move):
                        arr.append(comp(locn, locn + k * move))
                    break
                else:
                    break
                # elif inbrd(locn + k*move) and piecearray[tuple(locn + k*move)] * value > 0:
                #     break
    elif value == 900 or value == -900:
        moves = np.array([
            [1, 1], [-1, 1], [-1, -1], [1, -1], [0, -1], [
                0, 1], [1, 0], [-1, 0]])
        for move in moves:
            for k in range(1, 8):
                if inbrd(locn + k * move) and piecearray[tuple(locn + k * move)] == 0:
                    if makepseudomove(locn, locn + k * move):
                        arr.append(comp(locn, locn + k * move))
                elif inbrd(locn + k * move) and piecearray[tuple(locn + k * move)] * np.sign(value) < 0:
                    if makepseudomove(locn, locn + k * move):
                        arr.append(comp(locn, locn + k * move))
                    break
                else:
                    break
                # elif inbrd(locn + k*move) and piecearray[tuple(locn +k* move)] * value > 0:
                #     break

    elif value == 1000 or value == -1000 or value == 1001 or value == -1001:
        moves = np.array([
            [1, 1], [-1, 1], [-1, -1], [1, -1], [0, -1], [
                0, 1], [1, 0], [-1, 0]])
        for move in moves:
            if inbrd(locn + move) and piecearray[tuple(locn + move)] * np.sign(value) <= 0:
                if makepseudomove(locn, locn + move):
                    arr.append(comp(locn, locn + move))

    Castlable = CanCastle(value)
    if Castlable:
        arr.append(Castlable)


def Search(depth, alpha, beta, player):



    if depth == 0:
        return Evaluation(player)

    print("hELLO")

    # getallmoves()

    # if len(moves) == 0:
    #     if inCheck == True:
    #         return -10000
    #     else:
    #         return 0
    AI_moves_array = []
    for i in range(8):
        for j in range(8):
            if piecearray[i, j] * (-1 ** player) > 0:
                getallmoves(piecearray[i, j], np.array([i, j]), AI_moves_array)

    for move_val in AI_moves_array:
        if type(move_val) == str:
            CastleMove(move_val)

            player += 1
            gain = -Search(depth - 1, -beta, -alpha, player)
            player -= 1
            UndoCastleMove(move_val)
        else:
            locn_new = ((move_val//100)//8 , (move_val//100)%8)
            locn_old = ((move_val % 100) // 8, (move_val % 100) % 8)
            pieceval = piecearray[locn_old]
            attackval = piecearray[locn_new]
            piecearray[locn_old] = 0
            piecearray[locn_new] = pieceval


            player += 1
            # Compute
            gain = -Search(depth - 1, -beta, -alpha, player)
            player -= 1
            # UndoMove
            piecearray[tuple(locn_old)] = pieceval
            piecearray[tuple(locn_new)] = attackval

            if depth == Depth_Searched:
                return move_val

            if gain >= beta:
                return beta
            alpha = max(alpha, gain)
        #print(alpha)
        return alpha
    # for piece in piece_group[player % 2]:
    #     moves.clear()
    #     piece.get_moves(moves)
    #     locn_old = piece.location
    #     for locn_new in moves:
    #         if type(locn_new) == str:
    #             CastleMove(locn_new)
    #
    #             player += 1
    #             gain = -Search(depth - 1, -beta, -alpha, player)
    #             player -= 1
    #             UndoCastleMove(locn_new)
    #
    #         else:
    #             # MakeMove
    #             pieceval = piecearray[tuple(locn_old)]
    #             attackval = piecearray[tuple(locn_new)]
    #             piecearray[tuple(locn_old)] = 0
    #             piecearray[tuple(locn_new)] = pieceval
    #             piece.location = locn_new
    #
    #             player += 1
    #             # Compute
    #             gain = -Search(depth - 1, -beta, -alpha, player)
    #             player -= 1
    #             # UndoMove
    #             piecearray[tuple(locn_old)] = pieceval
    #             piecearray[tuple(locn_new)] = attackval
    #             piece.location = locn_old


    # for move in moves:
    #     DoMove()
    #     gain = -Search(depth-1, -beta , -alpha)
    #     UndoMove()
    #     if gain >= beta:
    #         return beta
    #     alpha = max(alpha,gain)


def MoveGetterAI():
    print("HEllo")
    return Search(Depth_Searched, -10000, 10000, 1)
