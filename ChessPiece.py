import pygame
import numpy as np
import os
from settings import *


#setting_init()

def globalloc(location):
    loc = (int(LEFTGAP + BOARDSQ/2 +((location[0])*BOARDSQ)) , int(BORDER + BOARDSQ/2 + ((7-location[1])*BOARDSQ)))
    return loc

def inbrd(location):
    if (0 <= location[0] < 8) and (0 <= location[1] < 8):
        return True
    else:
        return False


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
            self.isInf = False
            self.moves = np.array([[0, 1]])
            self.movespl = np.array([[-1, 1], [1, 1]])
        elif self.type == 'p':
            self.isInf = False
            self.moves = np.array([[1, 1]])
            self.movespl = np.array([[1, 1], [-1, 1]])

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







    def draw_possible_moves(self):
        if self.type == 'P':
            move = self.moves[0]
            if inbrd(self.location + move) and piecearray[tuple(self.location + move)] == 0:
                selectionbrd.add(possible_move(self.location + move))
            if self.location[1] == 1 and piecearray[tuple(self.location + 2*move)] == 0 :
                selectionbrd.add(possible_move(self.location + 2*move))
            if inbrd(self.location + move) and piecearray[tuple(self.location + self.movespl[0])] < 0:
                selectionbrd.add(possible_move(self.location + self.movespl[0]))
            if inbrd(self.location + move) and piecearray[tuple(self.location + self.movespl[1])] < 0:
                selectionbrd.add(possible_move(self.location + self.movespl[1]))
        elif self.isInf:

            for move in self.moves:
                print(move)
                k = 1
                # print(inbrd(self.location + k*move))
                print(self.location + k*move)
                #print(piecearray[tuple(self.location + k*move)])
                print(piecearray)
                while inbrd(self.location + k*move) and piecearray[tuple(self.location + k*move)] == 0 :
                    print("Hi")
                    selectionbrd.add(possible_move(self.location + k*move))
                    k+=1
                if inbrd(self.location + k*move) and  piecearray[tuple(self.location + k*move)] < 0 :
                    selectionbrd.add(possible_move(self.location + k*move))

        else:
            for move in self.moves:
                print(move)
                # print(inbrd(self.location + k*move))
                print(self.location + move)
                #print(piecearray[tuple(self.location + k*move)])
                print(piecearray)
                if inbrd(self.location + move) and piecearray[tuple(self.location + move)] == 0 :
                    print("Hi")
                    selectionbrd.add(possible_move(self.location + move))
                elif inbrd(self.location + move) and  piecearray[tuple(self.location + move)]  < 0 :
                    selectionbrd.add(possible_move(self.location + move))


    def update(self, location):
        piecearray[tuple(self.location)] = 0
        self.location = location
        piecearray[tuple(self.location)] = 1
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