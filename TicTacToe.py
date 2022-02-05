import sys, pygame
import numpy as np
from GameState import GameState
from MinMax import minimax
    
class TicTacToe:

	def __init__(self, size=(600, 600)):

		self.size = self.width, self.height = size

		# Colors
		self.BACKGROUND_COLOR = (20, 70, 100)
		self.WHITE_COLOR = (255, 255, 255)
		self.CIRCLE_COLOR = (140, 146, 172)
		self.CROSS_COLOR = (140, 146, 172)

		pygame.init()
		self.restart_game()


	def draw_game(self):
		offset = self.width / 100 * 7
		pygame.draw.line(self.screen, self.WHITE_COLOR, (self.width // 3, 0 + offset), (self.width // 3, self.width - offset), width=4)
		pygame.draw.line(self.screen, self.WHITE_COLOR, (2 * self.width // 3, 0 + offset), (2 * self.width // 3, self.width - offset), width=4)
		pygame.draw.line(self.screen, self.WHITE_COLOR, (0 + offset, self.width // 3), (self.width - offset, self.width // 3), width=4)
		pygame.draw.line(self.screen, self.WHITE_COLOR, (0 + offset, 2 * self.width // 3), (self.width - offset, 2 * self.width // 3), width=4)


	def draw_circle(self, x, y):
		radius = self.width / 100 * 8
		pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (self.width // 6 + self.width // 3 * y, self.width // 6 + self.width // 3 * x), radius, width=8)
		pygame.display.update()


	def draw_cross(self, x, y):
		radius = self.width / 100 * 8
		centre_pos = (self.width // 6 + self.width // 3 * y, self.width // 6 + self.width // 3 * x)
		pygame.draw.line(self.screen, self.CROSS_COLOR, (centre_pos[0] - radius, centre_pos[1] - radius), (centre_pos[0] + radius, centre_pos[1] + radius), width=8)
		pygame.draw.line(self.screen, self.CROSS_COLOR, (centre_pos[0] - radius, centre_pos[1] + radius), (centre_pos[0] + radius, centre_pos[1] - radius), width=8)
		pygame.display.update()


	def position_to_index(self, x, y):
		return y // (self.width / 3), x // (self.width / 3)


	def change_turn(self):

		if(self.game_state.turn_O):
			pygame.display.set_caption("Tic Tac Toe - O's turn")
		else:
			pygame.display.set_caption("Tic Tac Toe - X's turn")


	def is_game_over(self):

		is_game_over = self.game_state.is_terminal()

		winner = self.game_state.winner

		if winner == "O":
			pygame.display.set_caption("Game over - O won")
		elif winner == "X":
			pygame.display.set_caption("Game over - X won")
		elif winner == "Draw":
			pygame.display.set_caption("Draw")

		return is_game_over


	def restart_game(self):

		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Tic Tac Toe - O's turn")
		self.screen.fill(self.BACKGROUND_COLOR)

		self.draw_game()

		turn_O = True
		board_state = np.zeros((3, 3))
		self.game_state = GameState(board_state, turn_O)

		pygame.display.update()


	def move(self, move):
		self.game_state = self.game_state.get_new_state(move)


	def play_ai(self):

		minimax_score, move = minimax(self.game_state, 10, False)

		x = move[0]
		y = move[1]

		self.move((x, y))
		self.draw_cross(x, y)


		self.change_turn()
		self.is_game_over()
		pygame.display.update()


	def play(self, mode='player_vs_player'):
		"""
		:param: mode a mode in ['player_vs_player', 'player_vs_ai']
		"""
		while 1:

		    for event in pygame.event.get():

		    	if event.type == pygame.QUIT:
		    		sys.exit()

		    	if self.is_game_over():

		    		if event.type == pygame.MOUSEBUTTONUP:
		    			self.restart_game()
		    		continue

		    	if event.type == pygame.MOUSEBUTTONUP:
		    		x, y = self.position_to_index(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

		    		if self.game_state.turn_O:

		    			if self.game_state.board_state[int(x), int(y)] == 0:
		    				self.draw_circle(x, y)
		    				self.move((int(x), int(y)))
		    				self.change_turn()

		    				if mode == 'player_vs_ai':
		    					if not self.is_game_over():
		    						self.play_ai()

		    		else:

		    			if mode == 'player_vs_player':

			    			if self.game_state.board_state[int(x), int(y)] == 0:
			    				self.draw_cross(x, y)
			    				self.move((int(x), int(y)))
			    				self.change_turn()

		    		

		    pygame.display.update()


game = TicTacToe()
game.play(mode='player_vs_ai')
