#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from tetris import const,state

from pygame.locals import *

def terminate(error=0):
	pygame.quit()
	sys.exit(error)

def check_if_line(game_state):
	rows = [0 for x in range(0,const.WELL_H)]
	val = 0
	y = const.WELL_H
	while y > 0:
		y -= 1
		x = const.WELL_W
		complete = True
		while x > 0:
			x -= 1
			if game_state.well[y][x] == 0:
				complete = False
				break
		if complete == True:
			game_state.score += 1
			val += 1
			if y in rows:
				for i in range(y+1,const.WELL_H):
					rows[i] -= 1
		rows[y] = y - val 
	
	y = const.WELL_H
	while y > 0:
		y -= 1
		x = const.WELL_W
		while x > 0:
			x -= 1
			if rows[y] < 0:
				game_state.well[y][x] = 0
			else:
				game_state.well[y][x] = game_state.well[rows[y]][x]
	return game_state

def draw_screen(surface,game_state):

	surface.fill((0,0,0))

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
																								const.MARGIN_TOP + y * const.BLOCK_SIZE,
																								const.BLOCK_SIZE,const.BLOCK_SIZE))
			x += 1
		y += 1

	#Draw current piece
	curr_left = const.MARGIN_LEFT + (game_state.piece_x * const.BLOCK_SIZE)
	curr_top = const.MARGIN_TOP + (game_state.piece_y * const.BLOCK_SIZE)
	curr_color = const.C_LIST[game_state.cur_piece[0][0]]

	pygame.draw.rect(surface,curr_color,(curr_left,curr_top,
																			const.BLOCK_SIZE,const.BLOCK_SIZE))

	
	score(surface,game_state.score)
	pygame.display.update()

def score(surface,score):
	font = pygame.font.SysFont('monospace',20)
	text = font.render("Score : "+str(score),True,const.C_RED)
	surface.blit(text,(50,10))

def main():
	pygame.init()
	displaysurf = pygame.display.set_mode((const.SCR_W,const.SCR_H))
	game_state = state.GameState()
	while True:
		game_state = check_if_line(game_state)
		dx = 0
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if (game_state.piece_x - 1) >= 0 and game_state.well[game_state.piece_y][game_state.piece_x - 1] == 0: 
						dx = -1
				elif event.key == pygame.K_RIGHT:
					if (game_state.piece_x + 1) < const.WELL_W and game_state.well[game_state.piece_y][game_state.piece_x + 1] == 0:
						dx = 1
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					dx = 0

		#game logic
		if game_state.cur_piece == None:
			game_state.spawn_piece()

		game_state.piece_x += dx

		if game_state.piece_x < 0:
			game_state.piece_x = 0
		if game_state.piece_x >= const.WELL_W:
			game_state.piece_x = const.WELL_W - 1

		if game_state.piece_y < const.WELL_H - 1 and game_state.well[game_state.piece_y + 1][game_state.piece_x] == 0:
				game_state.piece_y += 1
		else:
			game_state.well[game_state.piece_y][game_state.piece_x] = game_state.cur_piece[0][0]
			game_state.spawn_piece()

		#display
		draw_screen(displaysurf,game_state)
		pygame.time.delay(60)

if __name__ == '__main__':
	main()
