#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from tetris import const,state

from pygame.locals import *

def terminate(error=0):
	pygame.quit()
	sys.exit(error)

def draw_screen(surface,game_state):

	#Draw well with border
	pygame.draw.rect(surface,const.C_LGRAY,(const.MARGIN_LEFT - 5,const.MARGIN_TOP - 5,
																					const.WELL_PX_W + 10,const.WELL_PX_H + 10))

	pygame.draw.rect(surface,const.C_DGRAY,(const.MARGIN_LEFT,const.MARGIN_TOP,
																					const.WELL_PX_W,const.WELL_PX_H))

	#Draw blocks
	y = 0
	while y < const.WELL_H:
		x = 0
		while x < const.WELL_W:
			curr = game_state.well[y][x]
			if curr != 0:
				current_color = const.C_LIST[curr]
				pygame.draw.rect(surface,current_color,(const.MARGIN_LEFT + x * const.BLOCK_SIZE,
																								const.MARIN_TOP + y * const.BLOCK_SIZE,
																								const.BLOCK_SIZE,const.BLOCK_SIZE))
			x += 1
		y += 1
	
	pygame.display.flip()

def main():
	pygame.init()
	displaysurf = pygame.display.set_mode((const.SCR_W,const.SCR_H))
	game_state = state.GameState()
	while True:
		#display

		draw_screen(displaysurf,game_state)

		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()

if __name__ == '__main__':
	main()
