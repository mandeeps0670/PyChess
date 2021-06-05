import numpy as np
import pygame

def setting_init():
    global HEIGHT
    global WIDTH
    global BORDER
    global BOARDL
    global BOARDSQ
    global LEFTGAP
    global FEN
    global piecearray
    global attack_array_b
    global attack_array_w

#Make sure Boardl%8 == 0, else weird tearing issues
   
HEIGHT = 720
WIDTH = 1000
BORDER = 64
BOARDL = HEIGHT - 2*BORDER
BOARDSQ = BOARDL/8         
LEFTGAP = (WIDTH-BOARDL)/2
FEN = list('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
piecearray = np.zeros((8,8),dtype=np.int16)
attack_array_b = np.zeros((8,8),dtype=np.int16)
attack_array_w = np.zeros((8,8),dtype=np.int16) 
  
white_pieces = pygame.sprite.Group()
black_pieces = pygame.sprite.Group()    
selectionbrd = pygame.sprite.Group()

screen = pygame.display.set_mode((WIDTH,HEIGHT))