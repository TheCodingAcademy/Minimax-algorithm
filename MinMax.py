from GameState import GameState


def  minimax(game_state : GameState, depth : int, maximizingPlayer : bool, alpha=float('-inf'), beta=float('inf')):

	if (depth==0) or (game_state.is_terminal()):
		return game_state.score(), None

	if maximizingPlayer:
		value = float('-inf')
		possible_moves = game_state.get_possible_moves()
		for move in possible_moves:
			child = game_state.get_new_state(move)

			tmp = minimax(child, depth-1, False, alpha, beta)[0]
			if tmp > value:
				value = tmp
				best_movement = move

			if value >= beta:
				break
			alpha = max(alpha, value)

	else:
		value = float('inf')
		possible_moves = game_state.get_possible_moves()
		for move in possible_moves:
			child = game_state.get_new_state(move)

			tmp = minimax(child, depth-1, True, alpha, beta)[0]
			if tmp < value:
				value = tmp
				best_movement = move

			if value <= alpha:
				break
			beta = min(beta, value)

	return value, best_movement
	