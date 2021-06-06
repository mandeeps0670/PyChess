import pygame
import os
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
from settings import *
from ChessPiece import typepiece

# setting_init()


FPS = 15
drk_sq = (118, 150, 86)
light_sq = (238, 238, 210)

pygame.init()

piece_selected = None



def pieceval(piece):
    if piece == 'p' or piece == 'P':
        return 1
    elif piece == 'n' or piece == 'N':
        return 3
    elif piece == 'b' or piece == 'B':
        return 3
    elif piece == 'r' or piece == 'R':
        return 5
    elif piece == 'q' or piece == 'Q':
        return 9
    elif piece == 'k' or piece == 'K':
        return 100

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
                piecearray[tuple(location)] = pieceval(piece)
            else:
                black_pieces.add(typepiece(piece, location))
                piecearray[tuple(location)] = -1*pieceval(piece)
            rank += 1


def drawboard():
    screen.fill((30, 30, 30))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                pygame.draw.rect(screen, drk_sq, [LEFTGAP + i * BOARDSQ, BORDER + j * BOARDSQ, BOARDSQ, BOARDSQ])
            else:
                pygame.draw.rect(screen, light_sq, [LEFTGAP + i * BOARDSQ, BORDER + j * BOARDSQ, BOARDSQ, BOARDSQ])


pygame.display.set_caption("Lets Play Chess")


def main():
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
                        piece_selected.update(selects.location)
                selectionbrd.empty()
                for whitepiece in white_pieces:
                    if whitepiece.rect.collidepoint(event.pos):
                        piece_selected = whitepiece
                        whitepiece.draw_possible_moves()


        drawboard()
        selectionbrd.draw(screen)

        white_pieces.draw(screen)
        black_pieces.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
