
import pygame
import os
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN

import ChessPiece
import settings
from settings import *
from ChessPiece import typepiece, possible_move



def pieceval(piece):
    if piece.isupper():
        if piece == 'P':
            return 100
        elif piece == 'N':
            return 302
        elif piece == 'B':
            return 300
        elif piece ==  'R':
            return 501
        elif piece == 'Q':
            return 900
        elif piece == 'K':
            return 1001
    else:
        if piece == 'p':
            return -100
        elif piece == 'n' :
            return -302
        elif piece == 'b' :
            return -300
        elif piece == 'r':
            return -501
        elif piece == 'q':
            return -900
        elif piece == 'k':
            return -1001

FPS = 15
drk_sq = (118, 150, 86)
light_sq = (238, 238, 210)
flag = 0
pygame.init()

piece_selected = None


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('CHECK MATE', True, (255,0,0),(255,255,0))


textRect = text.get_rect()

textRect.center = (WIDTH // 2, HEIGHT // 2)


def initialiseboard():
    file = 7
    rank = 0
    for piece in FEN:
        if piece == '/':
            rank = 0
            file -= 1
        elif piece.isdigit():
            rank += int(piece)
        else:

            location = np.array([rank, file])

            if piece.isupper():
                white_pieces.add(typepiece(piece, location))
            else:
                black_pieces.add(typepiece(piece, location))
            piecearray[tuple(location)] = pieceval(piece)
            rank += 1


def drawboard():
    screen.fill((30, 30, 30))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                pygame.draw.rect(screen, drk_sq, [LEFTGAP + i * BOARDSQ, BORDER + j * BOARDSQ, BOARDSQ, BOARDSQ])
            else:
                pygame.draw.rect(screen, light_sq, [LEFTGAP + i * BOARDSQ, BORDER + j * BOARDSQ, BOARDSQ, BOARDSQ])

def draw_possible_moves():
    for move in moves_array:
        selectionbrd.add(possible_move(move))



pygame.display.set_caption("Lets Play Chess")

moves
def main():
    CHECKMATE = False
    settings.moves
    #moves = 0
    run = True
    clock = pygame.time.Clock()
    drawboard()
    initialiseboard()
    # drawpiece()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                for selects in selectionbrd:
                    if selects.rect.collidepoint(event.pos):
                        print(piece_selected.type)
                        piece_selected.update(selects.location)
                        settings.moves += 1
                        t = ChessPiece.isCheckStaleMate()
                        if t:
                            if t == 10:
                                CHECKMATE = True
                            else:
                                print("Stale Mate")

                        print(piecearray)
                selectionbrd.empty()
                for piece in piece_group[settings.moves % 2]:
                    if piece.rect.collidepoint(event.pos):
                        piece_selected = piece
                        moves_array.clear()
                        piece.get_moves(moves_array)

                        draw_possible_moves()



        drawboard()
        selectionbrd.draw(screen)

        white_pieces.draw(screen)
        black_pieces.draw(screen)

        if CHECKMATE:
            screen.blit(text, textRect)


        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    setting_init()
    main()
