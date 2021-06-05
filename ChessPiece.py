import pygame
import os
from settings import *

#setting_init()

def globalloc(location):
    loc = (int(LEFTGAP + BOARDSQ/2 +((location[0])*BOARDSQ)) , int(BORDER + BOARDSQ/2 + ((7-location[1])*BOARDSQ)))
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
        
        if self.type.isupper():
            self.color = 'W'
        else:
            self.color = 'B'
        
        
        ## Pawns
        if self.type == 'P':
            isInf = False
            moves = [(0,-BOARDSQ)]
            movespl = [(-BOARDSQ,-BOARDSQ),(BOARDSQ,-BOARDSQ)]
        elif self.type == 'p':
            isInf = False
            moves = [(0,BOARDSQ)]
            movespl = [(BOARDSQ,BOARDSQ),(-BOARDSQ,BOARDSQ)]
            
        ## Rooks
        elif self.type == 'r' or self.type == 'R':
            isInf = True
            moves = [(0,-BOARDSQ),(0,BOARDSQ),(BOARDSQ,0),(-BOARDSQ,0)]
        
        ##Bishops
        elif self.type == 'b' or self.type == 'B':
            isInf = True
            moves = [(BOARDSQ,BOARDSQ),(-BOARDSQ,BOARDSQ),(-BOARDSQ,-BOARDSQ),(BOARDSQ,-BOARDSQ)]
            
        ##Kings
        elif self.type == 'k' or self.type == 'K':
            isInf = False
            moves = [(BOARDSQ,BOARDSQ),(-BOARDSQ,BOARDSQ),(-BOARDSQ,-BOARDSQ),(BOARDSQ,-BOARDSQ) , (0,-BOARDSQ),(0,BOARDSQ),(BOARDSQ,0),(-BOARDSQ,0) ]
            
        ##Queens
        elif self.type == 'q' or self.type == 'Q':
            isInf = True
            moves = [(BOARDSQ,BOARDSQ),(-BOARDSQ,BOARDSQ),(-BOARDSQ,-BOARDSQ),(BOARDSQ,-BOARDSQ) , (0,-BOARDSQ),(0,BOARDSQ),(BOARDSQ,0),(-BOARDSQ,0) ]
            
        ##Knights
        elif self.type == 'n' or self.type == 'N':
            isInf = False
            moves = [(2*BOARDSQ,BOARDSQ),(-2*BOARDSQ,BOARDSQ),(-2*BOARDSQ,-BOARDSQ),(2*BOARDSQ,-BOARDSQ) , (BOARDSQ,2*BOARDSQ),(-BOARDSQ,2*BOARDSQ),(-BOARDSQ,-2*BOARDSQ),(BOARDSQ,-2*BOARDSQ) ]

    def draw_possible_moves(self):
        if self.type == 'P':
            new_posn = (self.location[0] , self.location[1] + 1)
            selectionbrd.add(possible_move(new_posn))
            if self.location[1] == 1:
                new_posn = (self.location[0], self.location[1] + 2)
                selectionbrd.add(possible_move(new_posn))
    def update(self, location):
        self.location = location
        self.rect.center = globalloc(self.location)




class possible_move(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.location = location
        self.img = pygame.image.load(os.path.join('Images', 'selected.png'))
        self.image = pygame.transform.scale(self.img, (int(BOARDSQ), int(BOARDSQ)))
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = globalloc(self.location)