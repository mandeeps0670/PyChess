import pygame
import os
import numpy as np
from settings import *
from ChessPiece import typepiece

#setting_init()


FPS = 30
drk_sq = 	(118,150,86)
light_sq = 	(238,238,210)


pygame.init()
#init()



white_pieces = pygame.sprite.Group()
black_pieces = pygame.sprite.Group()



screen = pygame.display.set_mode((WIDTH,HEIGHT))
   

def initialiseboard():
    file = 7
    rank = 0
    for piece in FEN:
        if piece == '/':
            rank = 0
            file -=1
        elif piece.isdigit():
            rank += int(piece)
        else:
            rank+=1
            location = (rank,file)

            if piece.isupper():
                white_pieces.add(typepiece(piece,location))
            else:
                black_pieces.add(typepiece(piece,location))



def drawboard():
    screen.fill((30,30,30))
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 1:
                pygame.draw.rect(screen,drk_sq,[LEFTGAP + i*BOARDSQ, BORDER+j*BOARDSQ , BOARDSQ,BOARDSQ])
            else:
                pygame.draw.rect(screen,light_sq,[LEFTGAP + i*BOARDSQ, BORDER+j*BOARDSQ , BOARDSQ,BOARDSQ])




pygame.display.set_caption("Lets Play Chess") 

def main():
    run = True
    clock = pygame.time.Clock()
    drawboard()
    initialiseboard()
    #drawpiece()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        white_pieces.draw(screen)
        black_pieces.draw(screen)
        
        
        pygame.display.update()
        
                
    pygame.quit()
        
        
        
if __name__ == "__main__":
    main()