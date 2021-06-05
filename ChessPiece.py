import pygame
import os
from settings import *

#setting_init()

def globalloc(location):
    loc = (int(LEFTGAP + BOARDSQ/2 +((location[0]-1)*BOARDSQ)) , int(BORDER + BOARDSQ/2 + ((7-location[1])*BOARDSQ)))
    return loc


class typepiece(pygame.sprite.Sprite):
    
    def __init__(self,type,location):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.location = location
        self.type = type
        self.img = pygame.image.load(os.path.join('Images',type+'.png'))
        self.image = pygame.transform.scale(self.img,(int(BOARDSQ),int(BOARDSQ)))
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = globalloc(self.location)
        
        
        ## Pawns
        if type == 'P':
            isInf = False
            moves = [(0,-BOARDSQ)]
            movespl = [(-BOARDSQ,-BOARDSQ),(BOARDSQ,-BOARDSQ)]
        elif type == 'p':
            isInf = False
            moves = [(0,BOARDSQ)]
            movespl = [(BOARDSQ,BOARDSQ),(-BOARDSQ,BOARDSQ)]
            
        ## Rooks
        elif type == 'r' or type == 'R':
            isInf = True
            moves = [(0,-BOARDSQ),(0,BOARDSQ),(BOARDSQ,0),(-BOARDSQ,0)]
        
        ##Bishops
        elif type == 'b' or type == 'B':
            isInf = True
            moves = [(BOARDSQ,BOARDSQ),(-BOARDSQ,BOARDSQ),(-BOARDSQ,-BOARDSQ),(BOARDSQ,-BOARDSQ)]
            
        ##Kings
        elif type == 'k' or type == 'K':
            isInf = False
            moves = [(BOARDSQ,BOARDSQ),(-BOARDSQ,BOARDSQ),(-BOARDSQ,-BOARDSQ),(BOARDSQ,-BOARDSQ) , (0,-BOARDSQ),(0,BOARDSQ),(BOARDSQ,0),(-BOARDSQ,0) ]
            
        ##Queens
        elif type == 'q' or type == 'Q':
            isInf = True
            moves = [(BOARDSQ,BOARDSQ),(-BOARDSQ,BOARDSQ),(-BOARDSQ,-BOARDSQ),(BOARDSQ,-BOARDSQ) , (0,-BOARDSQ),(0,BOARDSQ),(BOARDSQ,0),(-BOARDSQ,0) ]
            
        ##Knights
        elif type == 'n' or type == 'N':
            isInf = False
            moves = [(2*BOARDSQ,BOARDSQ),(-2*BOARDSQ,BOARDSQ),(-2*BOARDSQ,-BOARDSQ),(2*BOARDSQ,-BOARDSQ) , (BOARDSQ,2*BOARDSQ),(-BOARDSQ,2*BOARDSQ),(-BOARDSQ,-2*BOARDSQ),(BOARDSQ,-2*BOARDSQ) ]