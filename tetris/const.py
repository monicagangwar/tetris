SCR_H = 670
SCR_W = 600

WELL_H = 20
WELL_W = 10

BLOCK_SIZE = 30

WELL_PX_H = BLOCK_SIZE * WELL_H
WELL_PX_W = BLOCK_SIZE * WELL_W

MARGIN_LEFT = 150
MARGIN_TOP = 50

C_BLACK	= (  0,   0,   0)
C_DGRAY	= ( 20,  20,  20)
C_LGRAY	= (255, 230, 255)
C_WHITE	= (255, 255, 255)
C_BROWN = (102, 51, 0)

C_CYAN   = (  0, 255, 255)
C_BLUE   = (  0,   0, 255)
C_ORANGE = (255, 128,   0)
C_YELLOW = (255, 255,   0)
C_GREEN  = (  0, 255,   0)
C_PURPLE = (200,   0, 200)
C_RED    = (255,   0,   0)
  
C_LIST = [C_BLACK,C_CYAN,C_BLUE,C_ORANGE,C_YELLOW,C_GREEN,C_PURPLE,C_RED,]

A = [[1,1,1,1],
		 [0,0,0,0],
		 [0,0,0,0],
		 [0,0,0,0]]

B = [[1,0,0,0],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0]]

C = [[1,1,0,0],
     [1,1,0,0],
     [0,0,0,0],
     [0,0,0,0]]

D = [[1,0,0,0],
     [1,0,0,0],
     [1,1,0,0],
     [0,0,0,0]]

E = [[1,1,0,0],
     [1,0,0,0],
     [1,0,0,0],
     [0,0,0,0]]

F = [[0,1,0,0],
     [1,1,0,0],
     [1,0,0,0],
     [0,0,0,0]]

G = [[0,1,0,0],
     [1,1,1,0],
     [0,0,0,0],
     [0,0,0,0]]

BLOCK_LIST = [A,B,C,D,E,F,G]
