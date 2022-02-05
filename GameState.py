
class GameState:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state
		self.turn_O = turn_O

		self.winner = ""


	def is_terminal(self):
		
		if(((self.board_state[0, 0] + self.board_state[0, 1] + self.board_state[0, 2]) == 3) or
		   ((self.board_state[1, 0] + self.board_state[1, 1] + self.board_state[1, 2]) == 3) or
		   ((self.board_state[2, 0] + self.board_state[2, 1] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 0] + self.board_state[1, 0] + self.board_state[2, 0]) == 3) or
		   ((self.board_state[0, 1] + self.board_state[1, 1] + self.board_state[2, 1]) == 3) or
		   ((self.board_state[0, 2] + self.board_state[1, 2] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 2] + self.board_state[1, 1] + self.board_state[2, 0]) == 3)):
				
				self.winner = "O"
				return True

		elif(((self.board_state[0, 0] + self.board_state[0, 1] + self.board_state[0, 2]) == -3) or
		     ((self.board_state[1, 0] + self.board_state[1, 1] + self.board_state[1, 2]) == -3) or
		     ((self.board_state[2, 0] + self.board_state[2, 1] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 0] + self.board_state[1, 0] + self.board_state[2, 0]) == -3) or
		     ((self.board_state[0, 1] + self.board_state[1, 1] + self.board_state[2, 1]) == -3) or
		     ((self.board_state[0, 2] + self.board_state[1, 2] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 2] + self.board_state[1, 1] + self.board_state[2, 0]) == -3)):
			
				self.winner = "X"
				return True

		is_there_free_cell = False
		for x in range(3):
			for y in range(3):
				if self.board_state[x, y] == 0:
					is_there_free_cell = True
		if (is_there_free_cell == False):
			self.winner = "Draw"
			return True
		else:
			self.winner = ""
			return False


	def score(self):
		
		if(((self.board_state[0, 0] + self.board_state[0, 1] + self.board_state[0, 2]) == 3) or
		   ((self.board_state[1, 0] + self.board_state[1, 1] + self.board_state[1, 2]) == 3) or
		   ((self.board_state[2, 0] + self.board_state[2, 1] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 0] + self.board_state[1, 0] + self.board_state[2, 0]) == 3) or
		   ((self.board_state[0, 1] + self.board_state[1, 1] + self.board_state[2, 1]) == 3) or
		   ((self.board_state[0, 2] + self.board_state[1, 2] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 2] + self.board_state[1, 1] + self.board_state[2, 0]) == 3)):
				
				return 1

		elif(((self.board_state[0, 0] + self.board_state[0, 1] + self.board_state[0, 2]) == -3) or
		     ((self.board_state[1, 0] + self.board_state[1, 1] + self.board_state[1, 2]) == -3) or
		     ((self.board_state[2, 0] + self.board_state[2, 1] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 0] + self.board_state[1, 0] + self.board_state[2, 0]) == -3) or
		     ((self.board_state[0, 1] + self.board_state[1, 1] + self.board_state[2, 1]) == -3) or
		     ((self.board_state[0, 2] + self.board_state[1, 2] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 2] + self.board_state[1, 1] + self.board_state[2, 0]) == -3)):
			
				return -1

		is_there_free_cell = False
		for x in range(3):
			for y in range(3):
				if self.board_state[x, y] == 0:
					is_there_free_cell = True
		if (is_there_free_cell == False):

			return 0
		else:
			return 0


	def get_possible_moves(self):
		
		moves = []
		for x in range(3):
			for y in range(3):
				if self.board_state[x, y] == 0:
					moves.append((x, y))
		return moves


	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x, y] = 1 if self.turn_O else -1
		return GameState(new_board_state, not self.turn_O)
		