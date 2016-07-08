#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
import time
from tetris import const,state

from pygame.locals import *

def terminate(error=0):
	pygame.quit()
	sys.exit(error)

def play_sound(path):
	sound = pygame.mixer.Sound('sounds/'+path)
	pygame.mixer.Sound.play(sound)
	pygame.mixer.music.stop()

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
			play_sound('SFX_SpecialTetris.ogg')
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

	surface.fill(const.C_LGRAY)

	#Draw well with border
	pygame.draw.rect(surface,const.C_DGRAY,(const.MARGIN_LEFT - 5,const.MARGIN_TOP - 5,
																					const.WELL_PX_W + 10,const.WELL_PX_H + 10))

	pygame.draw.rect(surface,const.C_WHITE,(const.MARGIN_LEFT,const.MARGIN_TOP,
																					const.WELL_PX_W,const.WELL_PX_H))

	#Draw blocks
	y = 0
	while y < const.WELL_H:
		x = 0
		while x < const.WELL_W:
			curr = game_state.well[y][x]
			if curr != 0:
				current_color = const.C_LIST[curr]
				pygame.draw.rect(surface,const.C_DGRAY,(const.MARGIN_LEFT + x * const.BLOCK_SIZE,
																								const.MARGIN_TOP + y * const.BLOCK_SIZE,
																								const.BLOCK_SIZE,const.BLOCK_SIZE))

				pygame.draw.rect(surface,current_color,(const.MARGIN_LEFT + x * const.BLOCK_SIZE - 1,
																								const.MARGIN_TOP + y * const.BLOCK_SIZE - 1,
																								const.BLOCK_SIZE - 1,const.BLOCK_SIZE - 1 ))
			x += 1
		y += 1

	#Draw current piece
	block_shape = const.BLOCK_LIST[game_state.cur_piece['shape']][game_state.rotate]
	curr_color = const.C_LIST[game_state.cur_piece['color']]
	for i in range(0,4):
		for j in range(0,4):
			if block_shape[i][j] == 1:
				curr_left = const.MARGIN_LEFT + ((game_state.piece_x + j) * const.BLOCK_SIZE)
				curr_top = const.MARGIN_TOP + ((game_state.piece_y + i) * const.BLOCK_SIZE)
				pygame.draw.rect(surface,const.C_DGRAY,(curr_left,curr_top,
																						const.BLOCK_SIZE,const.BLOCK_SIZE))

				pygame.draw.rect(surface,curr_color,(curr_left - 1,curr_top - 1,
																						const.BLOCK_SIZE - 1,const.BLOCK_SIZE - 1))
	
	score(surface,game_state.score)
	pygame.display.update()

def score(surface,score):
	font = pygame.font.SysFont('monospace',20)
	text = font.render("Score : "+str(score),True,const.C_RED)
	surface.blit(text,(const.MARGIN_LEFT,10))

def text_objects(text,font):
	textSurface = font.render(text,True,const.C_BROWN)
	return textSurface,textSurface.get_rect()

def message_display(surface,text):
	font = pygame.font.Font('freesansbold.ttf',30)
	textSurf,textRect = text_objects(text,font)
	textRect.center = ((const.SCR_W/2),(const.SCR_H/2))
	surface.blit(textSurf,textRect)
	pygame.display.update()
	time.sleep(4)
        get_exit_status()

def collision(game_state,diff_x,diff_y):
	block_shape = const.BLOCK_LIST[game_state.cur_piece['shape']][game_state.rotate]
	max_x = 0
	max_y = 0
	for i in range(0,4):
		for j in range(0,4):
			if block_shape[i][j] == 1:
				if j > max_x:
					max_x = j
				if i > max_y:
					max_y = i
				if game_state.piece_x + diff_x < 0:
					return True
				if game_state.piece_x + max_x + diff_x > const.WELL_W - 1:
					return True
				if game_state.piece_y + max_y + diff_y > const.WELL_H - 1:
					return True
				if game_state.well[game_state.piece_y + diff_y + i][game_state.piece_x + diff_x + j] != 0:
					return True	
	return False

def piece_lockdown(game_state):
	play_sound('SFX_PieceLockdown.ogg')
	block_shape = const.BLOCK_LIST[game_state.cur_piece['shape']][game_state.rotate]
	color = game_state.cur_piece['color']
	for i in range(0,4):
		for j in range(0,4):
			if block_shape[i][j] == 1:
				game_state.well[game_state.piece_y + i][game_state.piece_x + j] = color
	return game_state

def game():
	pygame.init()
	clock = pygame.time.Clock()
	loop = 0
	play_sound('SFX_GameStart.ogg')
	game_state = state.GameState()
	while True:
		game_state = check_if_line(game_state)
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if collision(game_state,-1,0) == False: 
						play_sound('SFX_PieceMoveLR.ogg')
						game_state.piece_x += -1
					else:
						play_sound('SFX_PieceTouchLR.ogg')
				elif event.key == pygame.K_RIGHT:
					if collision(game_state,1,0) == False:
						play_sound('SFX_PieceMoveLR.ogg')
						game_state.piece_x += 1
					else:
						play_sound('SFX_PieceTouchLR.ogg')
				elif event.key == pygame.K_SPACE:
					new_game_state = game_state
					new_game_state.rotate = (new_game_state.rotate + 1)%4
					if collision(new_game_state,0,0) == False:
						game_state = new_game_state
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					dx = 0

		#game logic
		if game_state.cur_piece == None:
			game_state.spawn_piece()


		if collision(game_state,0,1) == False:
				loop += 1
				if loop % 5 == 0:	
					game_state.piece_y += 1

		else:
			game_state = piece_lockdown(game_state)
			game_state.spawn_piece()
			if collision(game_state,0,0):
				block_shape = const.BLOCK_LIST[game_state.cur_piece['shape']][game_state.rotate]
				color = const.C_LIST[game_state.cur_piece['color']]
				for i in range(0,4):
					for j in range(0,4):
						if block_shape[i][j] == 1 and game_state.well[game_state.piece_y + i][game_state.piece_x + j] == 0:
							game_state.well[game_state.piece_y + i][game_state.piece_x + j] = color


				play_sound('SFX_GameOver.ogg')
				message_display(displaysurf,'Game ends. Your Score is ' + str(game_state.score))

		#display
		draw_screen(displaysurf,game_state)
		pygame.display.update()
		clock.tick(25)
#		pygame.time.delay(200)

def get_exit_status():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == K_n:
                    terminate()
                else:
                    game()
        displaysurf.fill(const.C_WHITE)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Continue? Y/N", largeText)
        TextRect.center = ((const.SCR_W/2),(const.SCR_H/2))
        displaysurf.blit(TextSurf, TextRect)
        pygame.display.update()
        pygame.time.delay(15)

displaysurf = pygame.display.set_mode((const.SCR_W,const.SCR_H))

def main():
	game()

if __name__ == '__main__':
	main()
