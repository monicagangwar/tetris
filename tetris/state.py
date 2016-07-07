from tetris import const
import random

class GameState(object):
	def __init__(self):
		super(GameState,self).__init__()
		self.init_well()
		self.level = 1
		self.score = 0
		self.cur_piece = None
		self.next_piece = None
		self.piece_x = 0
		self.piece_y = 0
	
	def init_well(self):
		self.well = []
		for y in range(0,const.WELL_H):
			row = []
			for x in range(0,const.WELL_W):
				row.append(0)
			self.well.append(row)

	def line_cleared(self):
		self.score += 1
		if self.score % 10 == 0 and self.score > 0:
			self.level += 1
	
	def get_new_piece(self):
		return {'color' : random.choice(range(1,8)), 'shape' : random.choice(range(0,7))}

	def spawn_piece(self):
		if self.next_piece == None:
			self.next_piece = self.get_new_piece()
		self.cur_piece = self.next_piece
		self.next_piece = self.get_new_piece()

		self.piece_x = 4 
		self.piece_y = 0
