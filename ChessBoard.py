import pygame
import os

pygame.init()

#Load All Images
r_image = pygame.image.load(os.path.join('Images','r.png'))
n_image = pygame.image.load(os.path.join('Images','n.png'))
b_image = pygame.image.load(os.path.join('Images','b.png'))
q_image = pygame.image.load(os.path.join('Images','q.png'))
k_image = pygame.image.load(os.path.join('Images','k.png'))
p_image = pygame.image.load(os.path.join('Images','p.png'))

R_image = pygame.image.load(os.path.join('Images','R.png'))
N_image = pygame.image.load(os.path.join('Images','N.png'))
B_image = pygame.image.load(os.path.join('Images','B.png'))
Q_image = pygame.image.load(os.path.join('Images','Q.png'))
K_image = pygame.image.load(os.path.join('Images','K.png'))
P_image = pygame.image.load(os.path.join('Images','P.png'))
################################################

HEIGHT = 480
WIDTH = 800
BORDER = 40
BOARDL = HEIGHT - 2*BORDER
BOARDSQ = BOARDL/8         #Make sure Boardl%8 == 0, else weird tearing issues
LEFTGAP = (WIDTH-BOARDL)/2
FPS = 30
drk_sq = 	(118,150,86)
light_sq = 	(238,238,210)
FEN = list('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
print(FEN)
screen = pygame.display.set_mode((WIDTH,HEIGHT))


class pieces:
    
    
    def __init__(self) -> None:
        pass
    
    

def drawpieces():
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
            location = (int(LEFTGAP+((rank-1)*BOARDSQ)) , int(BORDER + ((7-file)*BOARDSQ)))
            piecei= pygame.image.load(os.path.join('Images',piece+'.png'))
            pieceimg = pygame.transform.scale(piecei,(int(BOARDSQ),int(BOARDSQ)))
            screen.blit(pieceimg,location)
        



def drawboard():
    screen.fill((30,30,30))
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                pygame.draw.rect(screen,drk_sq,[LEFTGAP + i*BOARDSQ, BORDER+j*BOARDSQ , BOARDSQ,BOARDSQ])
            else:
                pygame.draw.rect(screen,light_sq,[LEFTGAP + i*BOARDSQ, BORDER+j*BOARDSQ , BOARDSQ,BOARDSQ])




pygame.display.set_caption("Lets Play Chess") 

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        drawboard()
        drawpieces()
        
        pygame.display.update()
        
                
    pygame.quit()
        
        
        
if __name__ == "__main__":
    main()