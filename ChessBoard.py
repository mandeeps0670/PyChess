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

HEIGHT = 640
WIDTH = 800
BORDER = 40
BOARDL = HEIGHT - 2*BORDER
BOARDSQ = BOARDL/8         #Make sure Boardl%8 == 0, else weird tearing issues
LEFTGAP = (WIDTH-BOARDL)/2
FPS = 30
drk_sq = 	(118,150,86)
light_sq = 	(238,238,210)
FEN = list('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
#print(FEN)

piece_list = []

white_pieces = pygame.sprite.Group()
black_pieces = pygame.sprite.Group()



screen = pygame.display.set_mode((WIDTH,HEIGHT))


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
        
        
        
        
            
            
def drawpiece():
    
    for boardpiece in piece_list:
            loc = (int(LEFTGAP+((boardpiece.location[0]-1)*BOARDSQ)) , int(BORDER + ((7-boardpiece.location[1])*BOARDSQ)))
            screen.blit(boardpiece.image,loc)           
    
    

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
            # piecei= pygame.image.load(os.path.join('Images',piece+'.png'))
            # pieceimg = pygame.transform.scale(piecei,(int(BOARDSQ),int(BOARDSQ)))
            #piece_list.append(typepiece(piece,location))
            #screen.blit(pieceimg,location)
            ##Color
            if piece.isupper():
                white_pieces.add(typepiece(piece,location))
            else:
                black_pieces.add(typepiece(piece,location))



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