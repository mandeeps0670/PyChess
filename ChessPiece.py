import pygame
import numpy as np
import os
import settings
from settings import *



# setting_init()
def pieceval(piece):
    if piece.isupper():
        if piece == 'P':
            return 100
        elif piece == 'N':
            return 302
        elif piece == 'B':
            return 300
        elif piece == 'R':
            return 500
        elif piece == 'Q':
            return 900
        elif piece == 'K':
            return 1000
    else:
        if piece == 'p':
            return -100
        elif piece == 'n':
            return -302
        elif piece == 'b':
            return -300
        elif piece == 'r':
            return -500
        elif piece == 'q':
            return -900
        elif piece == 'k':
            return -1000

def piecetyp(piece):
    if piece > 0:
        if piece == 100:
            return 'P'
        elif piece == 302:
            return 'N'
        elif piece == 300:
            return 'B'
        elif piece == 500 or piece == 501:
            return 'R'
        elif piece == 900:
            return 'Q'
        elif piece == 1000 or piece == 1001 :
            return 'K'
    else:
        if piece == -100:
            return 'p'
        elif piece == -302:
            return 'n'
        elif piece == -300:
            return 'b'
        elif piece == -500 or piece == -501:
            return 'r'
        elif piece == -900:
            return 'q'
        elif piece == -1000 or piece == -1001:
            return 'k'

def globalloc(location):
    loc = (
        int(LEFTGAP + BOARDSQ / 2 + ((location[0]) * BOARDSQ)),
        int(BORDER + BOARDSQ / 2 + ((7 - location[1]) * BOARDSQ)))
    return loc


def inbrd(location):
    if (0 <= location[0] < 8) and (0 <= location[1] < 8):
        return True
    else:
        return False

def respriteboard():
    piece_group[0].empty()
    piece_group[1].empty()
    for i in range(8):
        for j in range(8):
            if piecearray[i,j]:
                location = np.array([i,j])
                piece = piecetyp(piecearray[i,j])
                print(piece)
                if piece.isupper():
                    piece_group[0].add(typepiece(piece, location))
                else:
                    piece_group[1].add(typepiece(piece, location))

class typepiece(pygame.sprite.Sprite):

    def __init__(self, type, location):

        pygame.sprite.Sprite.__init__(self)

        self.location = location
        self.type = type
        self.img = pygame.image.load(os.path.join('Images', type + '.png'))
        self.image = pygame.transform.scale(self.img, (int(BOARDSQ), int(BOARDSQ)))
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = globalloc(self.location)

        if self.type.isupper():
            self.color = 'W'
        else:
            self.color = 'B'

        ## Pawns
        if self.type == 'P':
            self.isInf = False
            self.moves = np.array([[0, 1]])
            self.movespl = np.array([[-1, 1], [1, 1]])
        elif self.type == 'p':
            self.isInf = False
            self.moves = np.array([[0, -1]])
            self.movespl = np.array([[-1, -1], [1, -1]])

        ## Rooks
        elif self.type == 'r' or self.type == 'R':
            self.isInf = True
            self.moves = np.array([[0, -1], [0, 1], [1, 0], [-1, 0]])

        ##Bishops
        elif self.type == 'b' or self.type == 'B':
            self.isInf = True
            self.moves = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]])

        ##Kings
        elif self.type == 'k' or self.type == 'K':
            self.isInf = False
            self.moves = np.array([
                [1, 1], [-1, 1], [-1, -1], [1, -1], [0, -1], [
                    0, 1], [1, 0], [-1, 0]])


        ##Queens
        elif self.type == 'q' or self.type == 'Q':
            self.isInf = True
            self.moves = np.array([
                [1, 1], [-1, 1], [-1, -1], [1, -1], [0, -1], [
                    0, 1], [1, 0], [-1, 0]])

        ##Knights
        elif self.type == 'n' or self.type == 'N':
            self.isInf = False
            self.moves = np.array([
                [2, 1], [-2, 1], [-2, -1], [2, -1], [
                    1, 2], [-1, 2], [-1, -2], [1, -2]])

    def get_moves(self):
        moves_array.clear()

        if self.type == 'P':

            move = self.moves[0]
            ## move pawn 1 forward

            if inbrd(self.location + move) and piecearray[tuple(self.location + move)] == 0:
                moves_array.append(self.location + move)

            ## move 2 forward
            if self.location[1] == 1 and piecearray[tuple(self.location + 2 * move)] == 0 and piecearray[
                tuple(self.location + move)] == 0:
                moves_array.append(self.location + 2 * move)

            ## move sideways
            if inbrd(self.location + move) and inbrd(self.location + self.movespl[0]) and piecearray[
                tuple(self.location + self.movespl[0])] < 0:
                moves_array.append(self.location + self.movespl[0])

            ## move sideways
            if inbrd(self.location + move) and inbrd(self.location + self.movespl[1]) and piecearray[
                tuple(self.location + self.movespl[1])] < 0:
                moves_array.append(self.location + self.movespl[1])


        elif self.type == 'p':

            move = self.moves[0]
            ## move pawn 1 forward

            if inbrd(self.location + move) and piecearray[tuple(self.location + move)] == 0:
                moves_array.append(self.location + move)

            ## move 2 forward
            if self.location[1] == 6 and piecearray[tuple(self.location + 2 * move)] == 0 and piecearray[
                tuple(self.location + move)] == 0:
                moves_array.append(self.location + 2 * move)

            ## move sideways
            if inbrd(self.location + move) and inbrd(
                    self.location + self.movespl[0]) and piecearray[tuple(self.location + self.movespl[0])] > 0 :
                moves_array.append(self.location + self.movespl[0])

            ## move sideways
            if inbrd(self.location + move) and inbrd(
                    self.location + self.movespl[1]) and piecearray[tuple(self.location + self.movespl[1])] > 0 :
                moves_array.append(self.location + self.movespl[1])

        elif self.isInf:

            for move in self.moves:
                print(move)
                k = 1
                print(self.location + k * move)
                print(piecearray)
                while inbrd(self.location + k * move) and piecearray[tuple(self.location + k * move)] == 0:
                    print("Hi")
                    moves_array.append(self.location + k * move)
                    k += 1
                if inbrd(self.location + k * move) and (piecearray[tuple(self.location + k * move)] * pieceval(
                        self.type)) < 0:
                    moves_array.append(self.location + k * move)

        else:
            for move in self.moves:
                print(move)
                # print(inbrd(self.location + k*move))
                print(self.location + move)
                # print(piecearray[tuple(self.location + k*move)])
                print(piecearray)
                if inbrd(self.location + move) and piecearray[tuple(self.location + move)] == 0:
                    moves_array.append(self.location + move)
                elif inbrd(self.location + move) and (piecearray[tuple(self.location + move)] * pieceval(self.type)) < 0:
                    moves_array.append(self.location + move)

        if tuple(self.location) == (0, 0):
            if piecearray[0, 0] == 4 and piecearray[
                0, 1] == 0 and piecearray[0, 2] == 0 and piecearray[0, 3] == 0 and piecearray[0, 5] == 101:
                moves_array.append(np.array([0, 5]))

    def update(self, location):
        piecearray[tuple(self.location)] = 0
        self.location = location
        if pieceval(self.type)*piecearray[tuple(location)] < 0 :
            piecearray[tuple(self.location)] = pieceval(self.type)
            respriteboard()
        else:
            piecearray[tuple(self.location)] = pieceval(self.type)
        self.rect.center = globalloc(self.location)


class possible_move(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.location = location
        self.img = pygame.image.load(os.path.join('Images', 'SelectedSq.png'))
        self.image = pygame.transform.scale(self.img, (int(BOARDSQ), int(BOARDSQ)))
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = globalloc(self.location)
