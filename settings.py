import numpy as np
import pygame

def setting_init():
    global moves
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
    global  whiteincheck
    global blackincheck
    global CHECKMATE
    CHECKMATE = False

    

#Make sure Boardl%8 == 0, else weird tearing issues

whiteincheck  = False
blackincheck  = False

whitekinglocn = np.array([0,4])
blackkinglocn = np.array([7,4])


moves = 0



HEIGHT = 720
WIDTH = 1000
BORDER = 64
BOARDL = HEIGHT - 2*BORDER
BOARDSQ = BOARDL/8         
LEFTGAP = (WIDTH-BOARDL)/2
FEN = list('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
piecearray = np.zeros((8,8),dtype=np.int16)

attack_array = np.zeros((2,8,8),dtype=np.int8)
temp_attack_array = np.zeros((8,8),dtype=np.int8)

white_pieces = pygame.sprite.Group()
black_pieces = pygame.sprite.Group()    

piece_group = [white_pieces,black_pieces]

selectionbrd = pygame.sprite.Group()



moves_array = []

screen = pygame.display.set_mode((WIDTH,HEIGHT))

move_is_castle = False

CHECKMATE = False